class TriNode:
    def __init__(self, end=False):
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = TriNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TriNode()
            cur = cur.children[char]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return cur.end


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return True
        
        