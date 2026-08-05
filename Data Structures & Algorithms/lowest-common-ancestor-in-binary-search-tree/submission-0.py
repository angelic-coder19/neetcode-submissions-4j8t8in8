# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: Root of BST, Treenodes p and q
    Output: The Lowest Common Ancestor(LCA) of p and q in the tree

    - A node is considered its own decendent
    - There will be atleast two nodes in the BST
    - The node to the left is always smaller and the node to the right is larger

Match:
    - DFS

Planning:
    - Declare a stack to keep the last common ancestor
    - Keep two flags to indicate if the nodes have been found yet
        - Helper function to traverse BST and update stack
    
            - Base cases:
                - Switch flag if a node has been found
                - If we have found both p and q (check flags):
                    exit this function 
                
                - Add this node to the stack 
                
                - If both q and p are smaller than root
                    - Call function on Left half of BST
                
                - If both q and p are larger than root
                    - Call function on Right half of BST
                
                - If q and p are on different sides of root, we can exit
                    - return 
    Call helper function 
    If it exists then we can return the node at the top of the stack

    

"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = []
        P, Q = False, False
    
        def dfs(node):
            nonlocal stack, P, Q

            if node == p:
                P = True
            elif node == Q:
                Q = True
            
            if P and Q:
                return 
            
            stack.append(node)

            if q.val < node.val and p.val < node.val:
                dfs(node.left)
            
            if p.val > node.val and q.val > node.val:
                dfs(node.right)

            return
        dfs(root)
        return stack[-1]
