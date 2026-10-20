class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        