"""
Problem
- Adding new words and searching for existing words
- So we can implement a Trie to support linear word search

Strategy
- A trie node holds a dictionary of trie nodes and an end flag
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    """
    To add a word, you want to start at the root and iterate thru word
    - If the char exists in the children, then update cur
    - If the char doesn't exist, then we create a new TrieNode, add it to cur's children, and then update cur
    - want to mark the last char's end flag
    """
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.end = True

    """
    To search we go thru each char in word
    - If the char is in cur's children, then we continue on
    - If the char isn't in cur's chidren, then it's false
    - If we make it to the end we check if it's marked as end

    - In the case that we come across a '.', we're allowed to explore all possible children at that specific node. Then we can spawn another search for each child. 
    - If any of those come back True then we're good

    """
    def search(self, word: str) -> bool:
        return self.special_search(word, self.root, 0)
        
    
    def special_search(self, word, cur, start_idx):
        if start_idx == len(word):
            return cur.end
        
        for i in range(start_idx, len(word)):
            if word[i] == '.':
                for child in cur.children.values():
                    if self.special_search(word, child, i+1):
                        return True
                return False
            
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                return False

        return cur.end