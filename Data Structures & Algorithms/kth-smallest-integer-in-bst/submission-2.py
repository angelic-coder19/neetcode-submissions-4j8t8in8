# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order, queue = [], deque()

        queue.append(root)
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                order.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        order.sort()
        return order[k - 1]
