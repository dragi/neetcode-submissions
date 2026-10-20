class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(i, word, node):
            if not node.children and i < len(word):
                return False
            if i >= len(word):
                return node.end
            if word[i] == '.':
                for child in node.children:
                    if dfs(i+1, word, node.children[child]):
                        return True
            if word[i] in node.children:
                return dfs(i+1, word, node.children[word[i]])
            else:
                return False
        
        return dfs(0, word, self.trie)