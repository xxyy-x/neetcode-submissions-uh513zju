class TrieNode:
    def __init__(self):
        self.node = {}
        self.isend = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.node:
                cur.node[c] = TrieNode()
            cur = cur.node[c]
        cur.isend = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    # need dfs to do backtrack
                    for child in cur.node.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.node:
                        return False
                    cur = cur.node[c]
        
            return cur.isend

        res = dfs(0, self.root)
        return res

# ab.cc

# .aabcc


# need recusion when c = '.' to backtrack
# Trie 