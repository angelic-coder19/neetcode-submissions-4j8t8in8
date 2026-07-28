# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding: 
    Input: head of binary tree
    Output: The maximum depth of the binary tree

    - If a node is none, then there is no count there
    - We count the most nodes on a path and not the number of edges

Match: 
    Depth First Search, recursion

Plan: 
    - The goal is to go as deep as possible passing up the max number at each level 
    - The return value will accumulate the further down we go
    - Base case is when a node is None, return 0 
    - The recursive case is we return the max depth at each level
        - recursively call the funciton + 1 on the left child
        - recursively call the funciton + 1 on the right child
    - return the max of the two recursive calls 
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root: 
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left + 1, right + 1)