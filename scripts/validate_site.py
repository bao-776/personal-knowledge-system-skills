#!/usr/bin/env python3
"""Validate the static project's crawlability and essential search metadata."""
from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PUBLIC_ROOT = "https://bao-776.github.io/personal-knowledge-system-skills/"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.scripts: list[tuple[dict[str, str], str]] = []
        self._script_attrs: dict[str, str] | None = None
        self._script_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "title": self._in_title = True
        if tag == "meta": self.meta.append(values)
        if tag in {"a", "link"}: self.links.append(values)
        if tag == "script":
            self._script_attrs = values
            self._script_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title": self._in_title = False
        if tag == "script" and self._script_attrs is not None:
            self.scripts.append((self._script_attrs, "".join(self._script_text)))
            self._script_attrs = None

    def handle_data(self, data: str) -> None:
        if self._in_title: self.title += data
        if self._script_attrs is not None: self._script_text.append(data)


def validate_page(path: Path, expected_canonical: str) -> list[str]:
    errors: list[str] = []
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    description = next((m.get("content") for m in parser.meta if m.get("name") == "description"), None)
    canonical = next((l.get("href") for l in parser.links if l.get("rel") == "canonical"), None)
    alternates = {(l.get("hreflang"), l.get("href")) for l in parser.links if l.get("rel") == "alternate"}
    if not 15 <= len(parser.title.strip()) <= 65: errors.append(f"{path}: title length must be 15-65")
    if not description or not 70 <= len(description) <= 180: errors.append(f"{path}: meta description length must be 70-180")
    if canonical != expected_canonical: errors.append(f"{path}: unexpected canonical {canonical!r}")
    if not {"zh-CN", "en", "x-default"}.issubset({lang for lang, _ in alternates}): errors.append(f"{path}: missing hreflang links")
    for required in ("og:title", "og:description", "og:image"):
        if not any(m.get("property") == required and m.get("content") for m in parser.meta): errors.append(f"{path}: missing {required}")
    json_ld = [text for attrs, text in parser.scripts if attrs.get("type") == "application/ld+json"]
    if not json_ld: errors.append(f"{path}: missing JSON-LD")
    for value in json_ld:
        try: json.loads(value)
        except json.JSONDecodeError as exc: errors.append(f"{path}: invalid JSON-LD: {exc}")
    for attrs in parser.links:
        href = attrs.get("href", "")
        if not href or href.startswith(("http://", "https://", "#", "mailto:")): continue
        target = (path.parent / urlparse(href).path).resolve()
        if href.endswith("/"): target /= "index.html"
        if not target.exists(): errors.append(f"{path}: broken local link {href}")
    return errors


def main() -> int:
    errors = []
    errors += validate_page(SITE / "index.html", PUBLIC_ROOT)
    errors += validate_page(SITE / "en" / "index.html", PUBLIC_ROOT + "en/")
    preview = SITE / "assets" / "social-preview.png"
    if not preview.exists() or preview.read_bytes()[16:24] != (1200).to_bytes(4, "big") + (630).to_bytes(4, "big"):
        errors.append("social-preview.png must be a 1200x630 PNG")
    favicon = SITE / "assets" / "favicon.png"
    if not favicon.exists() or favicon.read_bytes()[16:24] != (64).to_bytes(4, "big") + (64).to_bytes(4, "big"):
        errors.append("favicon.png must be a 64x64 PNG")
    try: ElementTree.parse(SITE / "sitemap.xml")
    except (ElementTree.ParseError, OSError) as exc: errors.append(f"invalid sitemap.xml: {exc}")
    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    if PUBLIC_ROOT + "sitemap.xml" not in robots: errors.append("robots.txt does not advertise sitemap")
    if errors:
        print("SITE_CHECK_FAILED")
        print("\n".join(errors))
        return 1
    print("SITE_CHECK_OK pages=2 social_preview=1200x630 favicon=64x64 sitemap=valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
