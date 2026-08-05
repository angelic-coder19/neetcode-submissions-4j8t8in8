# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, queue = list(), deque()
        queue.append(root)
        while queue:
            level, n = [], len(queue)
            for _ in range(n):
                node = queue.popleft()
                if not node:
                    continue

                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            
            if level: 
                res.append(level)
        
        return res

