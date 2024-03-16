class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [TextNode("This is text with a `code block` word", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "`", "code")
        expected_nodes = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
