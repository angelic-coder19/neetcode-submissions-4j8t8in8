# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def maxDepth(root): 
            if not root:
                return 0
            
            right = maxDepth(root.right)
            left = maxDepth(root.left)

            self.res = max(self.res, right + left)

            return max(left, right) + 1

        maxDepth(root)
        
        return self.res