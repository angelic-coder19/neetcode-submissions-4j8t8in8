# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: root of binary tree
    Output: maximum path sum in the binary tree

    Constrataints/Edgecases:
    - A node can not appear in a path more than once
    - Path sum is the value of nodes in the tree
    - The path doesn't necessarily pass through the root node
    - We'll have at least one node in the tree

Match:
    - Depth Fist Search, - Global Variables - Hash Tables?

Planning:
    - Declare a gloabal varibale for the max path so far, set to 0

    - Declare a helper DFS function takes in a node as input, returns Nothing
        - Base case if the node is None: return 0
        - Calculate the path on the left by calling DFS function on left child
        - Calculate the path of the right by calling DFS function on right
        - Update global max if the larger (left + right) + node value is larger
    
    - Return the global variable 

"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val

        max_path = -float("inf")

        def dfs(node):
            nonlocal max_path

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            left_p, right_p = left + node.val, right + node.val
            circ_p = node.val if (node.val > left_p and node.val > right_p) else (left + right + node.val) 
            max_path = max(max_path, circ_p, left_p, right_p)
            return max(left, right, 0) + node.val
            
        dfs(root)
        return max_path








