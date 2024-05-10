from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node1 = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    node2 = TextNode('This is a text node', 'bold', 'https://www.boot.dev')

    htmlnode = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode)

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=[])
    
main()
