# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If we reach Leaf nodes
        if not p and not q:
            return True         

        # Base case 1: Only one node is None
        if not p and q or not q and p:
            return False

        # Base case 4: Node values are different
        if p.val != q.val:
            return False

        # Recursive case: Call same function on the left & right children of both nodes combine both left and right side
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)