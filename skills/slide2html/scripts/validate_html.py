#!/usr/bin/env python3
"""Static checks for standalone study HTML; Python standard library only.

Does not execute JS, fully parse CSS/HTML, or assess facts, accessibility, or layout.
External hyperlinks are allowed. Required assets must be embedded.
"""
import argparse
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.ids = Counter()
        self.fragments = []
        self.assets = []
        self.css = []
        self.title = []
        self.in_style = False
        self.in_title = False
        self.svg_depth = 0
        self.doctype = False
        self.charset = False
        self.viewport = False

    def handle_decl(self, decl):
        if decl.lower() == "doctype html":
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        if tag == "svg":
            self.svg_depth += 1
        if tag != "title" or self.svg_depth == 0:
            self.tags[tag] += 1
        a = dict(attrs)
        if a.get("id"):
            self.ids[a["id"]] += 1
        if tag == "meta":
            self.charset |= a.get("charset", "").lower() in ("utf-8", "utf8")
            self.viewport |= a.get("name", "").lower() == "viewport" and bool(a.get("content"))
        self.in_style |= tag == "style"
        self.in_title |= tag == "title" and self.svg_depth == 0
        if a.get("style"):
            self.css.append(a["style"])
        href = a.get("href", a.get("xlink:href", ""))
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(unquote(href[1:]))
        if href and urlsplit(href).scheme.lower() in ("javascript", "vbscript"):
            self.assets.append((tag, href))
        for attr in ("src", "poster", "srcset"):
            if attr in a:
                self.assets.append((tag + ":" + attr, a[attr]))
        if tag in ("image", "use") and href:
            self.assets.append((tag, href))
        if tag == "object" and a.get("data"):
            self.assets.append((tag, a["data"]))
        if tag == "link" and href:
            rels = a.get("rel", "").lower().split()
            if any(r in rels for r in ("stylesheet", "icon", "preload", "modulepreload", "manifest")):
                self.assets.append((tag, href))
        if tag == "iframe":
            self.assets.append((tag, a.get("src", "iframe needs manual review")))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "svg":
            self.svg_depth = max(0, self.svg_depth - 1)
        if tag == "style":
            self.in_style = False
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_style:
            self.css.append(data)
        if self.in_title:
            self.title.append(data)


def is_embedded(value):
    return value.strip().lower().startswith("data:") or value.strip().startswith("#")


def validate(path):
    """Return likely failures; an empty list means these static checks passed."""
    try:
        raw = Path(path).read_bytes()
    except OSError as exc:
        return [f"Cannot read file: {exc}"]
    if not raw.strip():
        return ["File is empty."]
    try:
        content = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return ["File is not valid UTF-8."]
    parser = PageParser()
    try:
        parser.feed(content)
        parser.close()
    except (ValueError, AssertionError) as exc:
        return [f"Could not parse markup: {exc}"]
    errors = []
    for tag in ("html", "head", "body", "title"):
        if parser.tags[tag] != 1:
            errors.append(f"Expected exactly one <{tag}>; found {parser.tags[tag]}.")
    if not parser.doctype:
        errors.append("Missing HTML5 doctype.")
    if not parser.charset:
        errors.append("Missing UTF-8 charset declaration.")
    if not parser.viewport:
        errors.append("Missing viewport declaration.")
    if not "".join(parser.title).strip():
        errors.append("Title is empty.")
    for ident, count in parser.ids.items():
        if count > 1:
            errors.append(f"Duplicate id: {ident}")
    for fragment in sorted(set(parser.fragments)):
        if fragment not in parser.ids:
            errors.append(f"Missing anchor target: #{fragment}")
    for tag, value in parser.assets:
        if not value or not is_embedded(value):
            errors.append(f"Non-embedded or unsupported asset ({tag}): {value[:120]}")
        elif tag.endswith(":srcset"):
            errors.append("srcset needs manual review; prefer one embedded src for static checks.")
    css = re.sub(r"/\*.*?\*/", "", "\n".join(parser.css), flags=re.S)
    if re.search(r"@import\b", css, re.I):
        errors.append("CSS @import is not supported in a self-contained file.")
    for value in re.findall(r"url\(\s*['\"]?(.*?)['\"]?\s*\)", css, re.I | re.S):
        if not is_embedded(value):
            errors.append(f"Non-embedded CSS asset: {value[:120]}")
        elif value.strip().startswith("#") and unquote(value.strip()[1:]) not in parser.ids:
            errors.append(f"Missing CSS fragment target: {value}")
    return errors


def main():
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument("html", type=Path)
    args = arg_parser.parse_args()
    errors = validate(args.html)
    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    print("PASS: basic structure, anchors, and static offline asset checks.")
    print("Still verify sources, translations, browser behavior, and rendered layout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
