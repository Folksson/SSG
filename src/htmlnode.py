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
