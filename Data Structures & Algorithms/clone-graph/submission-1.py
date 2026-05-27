"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        == 

        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        old_to_new = {}

        def dfs(oldnode):
            if oldnode in old_to_new:
                return old_to_new[oldnode]
            
            newNode = Node(oldnode.val) # we only want the value now, no neighborhood yet becaue that the old version
            old_to_new[oldnode] = newNode

            for nei in oldnode.neighbors:
                copy_nei = dfs(nei)
                newNode.neighbors.append(copy_nei)      


            return newNode
        
        return dfs(node)
        