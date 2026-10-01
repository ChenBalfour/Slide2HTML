"""Operational regression checks for the reusable static validator."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_html.py"
SPEC = importlib.util.spec_from_file_location("validate_html", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PAGE = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>学习页</title><style>body {color:#123}</style></head>
<body><a href="#topic">主题</a><main id="topic">知识</main></body></html>'''


class ValidationTests(unittest.TestCase):
    def check_page(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "page.html"
            path.write_text(text, encoding="utf-8")
            return MODULE.validate(path)

    def test_embedded_page_and_external_link(self):
        page = PAGE.replace("</body>", '<img alt="demo" src="data:image/png;base64,AA==">'
                            '<a href="https://example.org/paper">Source online</a></body>')
        self.assertEqual(self.check_page(page), [])

    def test_missing_and_duplicate_targets(self):
        errors = self.check_page(PAGE.replace('id="topic"', 'id="other"'))
        self.assertTrue(any("Missing anchor" in e for e in errors))
        errors = self.check_page(PAGE.replace("</body>", '<div id="topic"></div></body>'))
        self.assertTrue(any("Duplicate id" in e for e in errors))

    def test_remote_and_sibling_assets(self):
        for asset in ('<script src="https://cdn.example.org/app.js"></script>',
                      '<img src="figure.png" alt="figure">',
                      '<link rel="stylesheet" href="style.css">',
                      '<svg><image href="https://example.org/image.svg"/></svg>'):
            with self.subTest(asset=asset):
                self.assertTrue(self.check_page(PAGE.replace("</body>", asset + "</body>")))

    def test_css_dependencies(self):
        errors = self.check_page(PAGE.replace('color:#123', 'background:url(https://example.org/bg.png)'))
        self.assertTrue(any("CSS asset" in e for e in errors))
        errors = self.check_page(PAGE.replace('color:#123', '@import "font.css";'))
        self.assertTrue(any("@import" in e for e in errors))
        self.assertEqual(self.check_page(PAGE.replace('color:#123', 'filter:url(#topic)')), [])

    def test_invalid_encoding_and_empty_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "page.html"
            for data in (b"", b"\\xff"):
                path.write_bytes(data)
                self.assertTrue(MODULE.validate(path))

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(MODULE.validate(Path(directory) / "missing.html"))

    def test_accessible_svg_title_is_not_document_title(self):
        figure = '<svg role="img"><title>A concept diagram</title></svg>'
        self.assertEqual(self.check_page(PAGE.replace("</body>", figure + "</body>")), [])

    def test_document_title_is_still_required(self):
        page = PAGE.replace("<title>学习页</title>", "")
        page = page.replace("</body>", "<svg><title>Diagram</title></svg></body>")
        self.assertTrue(self.check_page(page))

    def test_demo(self):
        self.assertEqual(MODULE.validate(SCRIPT.parents[1] / "examples" / "slide2html.html"), [])


if __name__ == "__main__":
    unittest.main()
