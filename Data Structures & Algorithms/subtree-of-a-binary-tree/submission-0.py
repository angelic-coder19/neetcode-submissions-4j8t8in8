# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understanding:
    input: root of tree and a subtree
    output: True if subtree is exists within tree
            False if subtree noes not exit withing tree
        
    - The whole tree can be considered a subtree
    - The structure and node values have to be the same
Match:
    - Recursive DFS

Planning:
    - Start at root node 
    - Iterate recursively through the tree while keeping root of subroot still
    - If the value at a node matches the head of subroot, 
        - Pass head of tree and subtree to helper function for comparison
            - If both nodes are none: return True
            - If one of the nodes is None: return False
            - If values are not the same: return False
            - Recall helper left and right nodes of both nodes
        - If helper was not true: recursively call main function on child nodes
        - If helper returned True: return True

"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return (isSame(root.left, subRoot.left) 
                    and isSame(root.right, subRoot.right))
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if isSame(root, subRoot):
                return True
        
        return (self.isSubtree(root.left,subRoot) or
        self.isSubtree(root.right,subRoot))


            
