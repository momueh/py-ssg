import re
from textnode import TextNode


def main():

    def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            return LeafNode(None, text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode("b", text_node.text)
        elif text_node.text_type == "italic":
            return LeafNode("i", text_node.text)
        elif text_node.text_type == "code":
            return LeafNode("code", text_node.text)
        elif text_node.text_type == "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError(f"Unknown text_type: {text_node.text_type}")

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if not isinstance(node, TextNode):
                new_nodes.append(node)
                continue
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Invalid Markdown syntax")
            new_nodes.extend(
                TextNode(part, text_type if i % 2 else "text")
                for i, part in enumerate(parts)
            )
        return new_nodes

    def extract_markdown_images(text):
        return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    def extract_markdown_links(text):
        return re.findall(r"\[(.*?)\]\((.*?)\)", text)

    def split_nodes_image(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if not isinstance(node, TextNode):
                new_nodes.append(node)
                continue
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
                continue
            parts = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, "text"))
                else:
                    new_nodes.append(
                        TextNode(images[i // 2][0], "image", images[i // 2][1])
                    )
        return new_nodes

    def split_nodes_link(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if not isinstance(node, TextNode):
                new_nodes.append(node)
                continue
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
                continue
            parts = re.split(r"\[(.*?)\]\((.*?)\)", node.text)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, "text"))
                else:
                    new_nodes.append(
                        TextNode(links[i // 2][0], "link", links[i // 2][1])
                    )
        return new_nodes

    def text_to_textnodes(text):
        nodes = [TextNode(text, "text")]
        nodes = split_nodes_bold(nodes)
        nodes = split_nodes_italic(nodes)
        nodes = split_nodes_code(nodes)
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_link(nodes)
        return nodes


if __name__ == "__main__":
    main()
