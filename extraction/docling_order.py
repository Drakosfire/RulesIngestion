"""Conservative source-order repair for Docling document references."""
import re
import unicodedata



def normalize(text):
    text = re.sub(r'[-‐]\s*\n\s*', '', text)
    return ' ' + ' '.join(re.findall(r'\w+', unicodedata.normalize('NFKC', text).casefold())) + ' '


def location(text, native):
    needle = normalize(text)
    start = native.find(needle)
    if start < 0 or native.find(needle, start + 1) >= 0 or len(needle.split()) < 3:
        return None
    return start, start + len(needle)


def _repair_page(doc, pdf, target_page):
    refs = doc['body']['children']
    items = {x['self_ref']: x for x in doc['texts']}
    reports = []
    for h in range(len(refs)):
        heading = items.get(refs[h]['$ref'], {})
        if heading.get('label') != 'section_header':
            continue
        prov = heading.get('prov', [])
        if len(prov) != 1:
            continue
        page = prov[0]['page_no']
        if page != target_page:
            continue

        def text_at(i):
            if not 0 <= i < len(refs):
                return {}
            item = items.get(refs[i]['$ref'], {})
            sources = item.get('prov', [])
            return item if len(sources) == 1 and sources[0]['page_no'] == page else {}

        # An interrupted paragraph resumes with a lowercase fragment.
        end = h + 1
        while text_at(end).get('label') == 'text' and not text_at(end)['text'].lstrip()[:1].islower():
            end += 1
        continuation = text_at(end)
        if not continuation.get('text', '').lstrip()[:1].islower():
            continue
        start = h - 1
        while text_at(start).get('label') == 'text':
            start -= 1
        if text_at(start).get('label') != 'section_header' or start + 1 == h:
            continue
        native = normalize(pdf[page - 1].get_text(sort=False))
        moved = [location(text_at(i)['text'], native) for i in range(h, end)]
        split = [location(text_at(i)['text'], native) for i in range(start + 1, h)]
        tail = location(continuation['text'], native)
        if not tail or not all(moved) or not all(split):
            continue
        pairs = moved + split + [tail]
        if any(a[1] - 1 > c[0] for a, c in zip(pairs, pairs[1:])):
            continue
        # The native order must join the preceding paragraph directly to its tail.
        if native[split[-1][1] - 1:tail[0]].strip():
            continue
        if text_at(h - 1)['text'].rstrip().endswith(('.', '!', '?', ':', ';')):
            continue
        reports.append({'page': page, 'moves': [r['$ref'] for r in refs[h:end]], 'before': refs[start]['$ref']})
        doc['body']['children'] = refs[:start] + refs[h:end] + refs[start:h] + refs[end:]
        return reports  # One conservative change per page.
    return reports


def repair(doc, pdf):
    """Repair each page independently, regardless of conversion range."""
    return [
        move
        for page in sorted(map(int, doc["pages"]))
        for move in _repair_page(doc, pdf, page)
    ]
