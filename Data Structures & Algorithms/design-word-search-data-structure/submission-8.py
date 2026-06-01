class TrieNode:
    def __init__(self, end=False):
        self.children = {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        
        cur.end = True
        

    def search(self, word: str) -> bool:
        return self.search_all(word, self.root, 0)

    def search_all(self, word: str, cur: TrieNode, start: int) -> bool:

        if start == len(word):
            return cur.end

        for index in range(start, len(word)):
            char = word[index]

            if char == ".":
                for child in cur.children.values():
                    if self.search_all(word, child, index + 1):
                        return True
                
                return False
            elif char not in cur.children:
                return False
            else:
                cur = cur.children[char]

        return cur.end 
        
