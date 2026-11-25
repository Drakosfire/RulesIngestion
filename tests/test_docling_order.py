from extraction.docling_order import repair


class NativePage:
    def __init__(self, text):
        self.text = text

    def get_text(self, *, sort):
        assert sort is False
        return self.text


def docling_order_fixture():
    items = [
        ("section_header", "Encumbrance"),
        ("text", "This unfinished prose continues"),
        ("section_header", "Buying Equipment and Services"),
        ("text", "This different section has its own prose."),
        ("text", "on the other side."),
    ]
    texts = [
        {"self_ref": f"#/texts/{i}", "label": label, "text": text, "prov": [{"page_no": 1}]}
        for i, (label, text) in enumerate(items)
    ]
    return {
        "pages": {"1": {}},
        "texts": texts,
        "body": {"children": [{"$ref": item["self_ref"]} for item in texts]},
    }


def test_does_not_reverse_headings_without_native_support():
    doc = docling_order_fixture()
    native = NativePage(
        "Encumbrance Buying Equipment and Services This different section has its own prose. "
        "This unfinished prose continues on the other side."
    )
    assert repair(doc, [native]) == []
    assert [x["$ref"] for x in doc["body"]["children"]] == [f"#/texts/{i}" for i in range(5)]


def test_repairs_when_native_heading_and_paragraph_order_agree():
    doc = docling_order_fixture()
    native = NativePage(
        "Encumbrance Buying Equipment and Services This different section has its own prose. "
        "Encumbrance This unfinished prose continues on the other side."
    )
    assert repair(doc, [native])
    assert [x["$ref"] for x in doc["body"]["children"]] == [
        f"#/texts/{i}" for i in (2, 3, 0, 1, 4)
    ]
