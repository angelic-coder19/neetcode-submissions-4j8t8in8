# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: root of binary tree
    Output: integer number of good nodes in the binary tree

    - A good node is one with the highest value in the path from the root node
    
Match:
    - DFS - Helper functions

Planning:
    - set a global variable for count of good nodes

    - Declare a DFS helper function it will take a node and max_parent
        - If a node is none: we have reach a leaf so we return 
        - If node's value is greater than max parent, 
            - increment global count 
        
        - update max_parent and pass to left child
        - update max_parent and pass to right child

    - Call DFS function with root node and - infinity so the root can always be good
    - Return global count  



"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, max_parent): 
            nonlocal count
            
            if not node:
                return 
            
            if node.val >= max_parent:
                count += 1
                max_parent = node.val
            
            dfs(node.left, max_parent)
            dfs(node.right, max_parent)
        
        dfs(root, -float("inf"))
        return count





