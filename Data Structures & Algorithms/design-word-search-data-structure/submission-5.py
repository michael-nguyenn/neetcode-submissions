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
        return self.search_all(word, self.root)

    def search_all(self, word: str, cur: TrieNode) -> bool:

        if word == "":
            return cur.end

        for index, char in enumerate(word):
            if char == ".":
                for child in cur.children:
                    if self.search_all(word[index+1:], cur.children[child]):
                        return True
                
                return False
            elif char not in cur.children:
                return False
            else:
                cur = cur.children[char]

        return cur.end 
        
