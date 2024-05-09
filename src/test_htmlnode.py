import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="p")
        print(node)
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Heading", children=[], props={"class": "heading"})
        expected_result = "HTMLNode(tag=h1, value=Heading, children=[], props={'class': 'heading'})"
        self.assertEqual(repr(node), expected_result)

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()