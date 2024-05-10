import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Heading", children=[], props={"class": "heading"})
        expected_result = "HTMLNode(tag=h1, value=Heading, children=[], props={'class': 'heading'})"
        self.assertEqual(repr(node), expected_result)

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        expected_result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_without_tag(self):
        node = LeafNode(value="This is some raw text.")
        expected_result = "This is some raw text."
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_empty_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_tag_and_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_result = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(children=[LeafNode("b", "Bold text")])

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=[])

    def test_nested_parent_nodes(self):
        inner_node = ParentNode(
            tag="span",
            children=[
                LeafNode(None, "Nested text")
            ]
        )
        outer_node = ParentNode(
            tag="div",
            children=[
                inner_node
            ]
        )
        expected_result = "<div><span>Nested text</span></div>"
        self.assertEqual(outer_node.to_html(), expected_result)

    def test_multiple_levels_of_nesting(self):
        innermost_node = ParentNode(
            tag="p",
            children=[
                LeafNode(None, "Innermost text")
            ]
        )
        inner_node = ParentNode(
            tag="div",
            children=[
                innermost_node
            ]
        )
        outer_node = ParentNode(
            tag="article",
            children=[
                inner_node
            ]
        )
        expected_result = "<article><div><p>Innermost text</p></div></article>"
        self.assertEqual(outer_node.to_html(), expected_result)


if __name__ == '__main__':
    unittest.main()