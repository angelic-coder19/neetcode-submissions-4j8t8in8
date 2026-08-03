# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding: 
    Input: The root of a binary tree
    Output: True if both left and right subtrees's height differ in height by less than 1
            False if subtrees differ in height by more than 1


    - A binary tree can be empty 
    - We count the number of edges and not the number of nodes
    - The number of edges is counted after a node is visited and passed on 
Match: 
    - DFS, Helper function

Planning:
    - 

"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root):

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left, right) + 1
        
        dfs(root)
        return self.balanced