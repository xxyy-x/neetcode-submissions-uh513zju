# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
import collections

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return None

        q = collections.deque()
        q.append(root)
        res = []

        while q:
            node = q.popleft()
            heapq.heappush(res, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)   
    
        for i in range(k-1):
            heapq.heappop(res)

        return res[0]
        

            
        
        

        
