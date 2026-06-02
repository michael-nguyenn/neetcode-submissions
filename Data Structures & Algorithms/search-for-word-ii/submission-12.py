class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()    
            cur = cur.children[c]
        cur.end = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # We're going to start building words, and if the words are marked
        # words in the Trie, then we can add to our res
        def dfs(row, col, node, word):

            if (row < 0 or col < 0 or 
            row == ROWS or col == COLS or 
            (row, col) in visited or 
            board[row][col] not in node.children):
                return False

            visited.add((row, col))

            # At this point on the board we know the child exists so we move
            # to that child and we explore 
            node = node.children[board[row][col]]
            word += board[row][col] # continue building the word

            # There's a chance the current node is a word
            if node.end: res.add(word)

            for r, c in directions:
                dfs(row + r, col + c, node, word)

            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        
        return list(res)

        

