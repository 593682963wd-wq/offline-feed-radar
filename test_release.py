"""作者：Wangyuan；日期：2026-11-08。职责：RSS身份与Atom正文/链接回归。"""
import unittest
from core import run


class FeedRegressions(unittest.TestCase):
    def test_distinct_ids_do_not_collide_after_slug_normalization(self) -> None:
        result = run({"xml": "<rss><channel><item><guid>post/1</guid><title>A</title></item><item><guid>post-1</guid><title>B</title></item></channel></rss>"})
        self.assertEqual(len(result["items"]), 2)

    def test_atom_uses_alternate_link_and_content_fallback(self) -> None:
        xml = '<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>synthetic</id><title>Title</title><link rel="alternate" href="https://example.invalid/page"/><link rel="self" href="https://example.invalid/item.xml"/><content type="text">unique-query-word</content></entry></feed>'
        result = run({"xml": xml, "query": "unique-query-word"})
        self.assertEqual(result["items"][0]["url"], "https://example.invalid/page")
        self.assertEqual(result["items"][0]["summary"], "unique-query-word")

    def test_invalid_xml_has_public_validation_error(self) -> None:
        with self.assertRaises(ValueError):
            run({"xml": "<rss>"})
