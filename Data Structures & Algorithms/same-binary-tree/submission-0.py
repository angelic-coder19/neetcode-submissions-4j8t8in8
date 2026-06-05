# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U:
    input: Roots of two binary trees
    output: True if trees are equivelent
            False if trees are not equivelent

    - Equivelent: same in both structure and node values
    - There can be a tree that doesn't have any nodes
M: 
    - Recursive DFS
P:
    - Start at the root of both nodes
    - If both trees are NOT empty: return False
    - If both nodes are NOT None: return False
    - If values at nodes are NOT the same: return False
    - Call the same function passing in left of p and left of q
    - Call the same function passin in right of p and right of q
    - Return True if 
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))





