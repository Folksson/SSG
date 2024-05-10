class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}  # Ensure props defaults to an empty dictionary

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_attributes = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
        return ' ' + html_attributes if html_attributes else ''

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if not value:
            raise ValueError("LeafNode value cannot be None")
    
    def to_html(self):
        if not self.tag:
            return self.value
        else:
            html_attributes = self.props_to_html()
            return f"<{self.tag}{html_attributes}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None or not children:
            raise ValueError("ParentNode must have children")

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"