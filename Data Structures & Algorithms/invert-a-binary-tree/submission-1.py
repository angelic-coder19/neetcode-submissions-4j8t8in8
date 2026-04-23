# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: root of binary tree
    Output: root of binary tree with all nodes on the left on the right and vice-versa

    - Each nodes left node must become the right node

Match:
    - Recursion

Planning:
    - For each node, left must become right, right must become left
    - Base case:
        - When there is no node
            - return None
        
        - We collect the left and the right nodes of that node
        - We assign right to left and left node to right
        - We call this function on each nodes left and right nodes
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
    
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) 
        self.invertTree(root.right)

        return root 
        