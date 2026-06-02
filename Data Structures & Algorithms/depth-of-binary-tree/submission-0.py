# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U:
    Input: Root of a binary tree
    Output: The maximum depth of the binary tree

    - Depth is the number of nodes along
M:

P:
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base case
        if not root:
            return 0

        if not root.right and not root.left:
            return 1

        # Recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 