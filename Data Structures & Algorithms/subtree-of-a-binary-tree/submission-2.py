# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U:
    input: Given Root and Subroot
    Ouput: True if subroot is a sub root of root

    - There will be atleast one node in both trees
    - The subtree has to be exactly the same as a whole subtree, not just a section

M:
    - Tree Comparison - DFS - Helper Fuction
P:
    - Create a helper function that will simply Check if two trees are the same
    - The main function will at each node check if the subtree starting from this node is the same as the subroot
    - Base cases:
        When the root is none, return False

    - If the tree is the same, return Tree immediately
    - At this point advance the Tree to see if a subroot exists in the left and right children  

"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isSame(p, q):
            if not p and not q:
                return True
            
            if not q and p or not p and q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSame(q.left, p.left) and isSame(q.right, p.right)

        if not root:
            return False
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        