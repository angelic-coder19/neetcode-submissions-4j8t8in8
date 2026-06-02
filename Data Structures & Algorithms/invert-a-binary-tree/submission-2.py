# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U:
    Input: root of binary tree
    Output: root of binary tree inverted

    - Inversion is left children becoming right children
    - If there is no node in bary tree, return empty tree

M:
 -DFS 

P:
    - Check if the tree is empty
    - Consider each sub-tree: Swap the left node with the right node
    - If The node is None, no swap: return 
    - If a node has one child or two children, swap left child and right child
    - Return the head of the binary tree
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        if root.left:
            self.invertTree(root.left)
        
        if root.right:
            self.invertTree(root.right)
        
        return root
                   
                