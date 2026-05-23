class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the tree of the all the words
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        ROW, COL = len(board), len(board[0])
        res = set() # the word we visit and we do not want to repeat
        visit = set() # In one word, we cannot visit the same character twice

        # Set up the dfs for each char in board

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == ROW or c == COL 
                or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord == True:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c))

        # call the dfs of each char
        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, root, "")

        return list(res)













