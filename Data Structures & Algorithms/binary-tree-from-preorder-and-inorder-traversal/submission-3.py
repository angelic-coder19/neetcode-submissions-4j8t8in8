# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: two integer arrays pre-order and in-order nodes 
    Output: the root of a binary tree assembled from the arrays

    - The two arrays are the same length
    - There are distinct values in both arrays

Match:
    - Binary Search     - Hash Tables

Planning: 
    - Declare a hash table to map values to corresponding nodes
    - The first element of preorder returns the root of the binary tree
    - Create a node with the first element of preorder
    - Find idex of the root node in the inorder array
    - Add this root node to the hash table with the value as a key
    - Set a variable to start at 0 (in the preorder array)
    - While this pointer is not equal to length of preorder:
        - Check if the value in preorder has a node in the hash table
            - if it does store it in node variable
        - If the node does not exist in hash table, create one
        - Index of the left node should be at (0 + ptr) // 2 in inorder array
        - if this index is equal to ptr - 1 in pre order: everything good
        - If not keep shifting forward until it is
            - Creat node, add it to hash table with the value as key

        - Index of the right node should be at ((ptr - 1) + len(n) - 1) // 2 in inorder
        - If the value at this index is not the same as ptr + 1 in preorder: shift back
        - If this value is not in dict: 
            - Create node for it, add to hash table with value as key
    
    - Return value of indexing into hash table with the first element in preorder array
    

"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
        """
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r: 
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1) 







