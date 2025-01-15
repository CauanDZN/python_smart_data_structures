class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

trie = Trie()
words = ["apple", "app", "banana", "bat"]
for word in words:
    trie.insert(word)

print("Search for 'apple':", trie.search("apple"))
print("Search for 'app':", trie.search("app"))
print("Search for 'bat':", trie.search("bat"))
print("Search for 'ball':", trie.search("ball"))
