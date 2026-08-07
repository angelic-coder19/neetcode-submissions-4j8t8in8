# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: root of a binary tree
    Output: True if the the tree is a Binary Search Tree (BST)

    It is a bst if:
      - Every subtree to the left of the node is a BST
      - The left children's vals must be less than the node
      - The right children's vals must be greater than the node's val
    
    - We can have one node in the BST

Match:
    - DFS  

Planning:
    - Base cases: 
        - If a node is None: return True // Because it is valid 
        - Check if this node has children to perform comparison
        - If the node's left node is greater or equal to node's: return False
        - If the node's right value is less than or equal to node's: return False
        - Call the result of checking the left and right
        // We can only return True if both sides reached the root node where they reached a true case

    - Left Helper takes in node, parent node
        - If this node is none, return True cause we have reached leaves
        - If this node has a left child and We keep going left: 
            - We ensure that keep getting larger (The child must be larger)
            - If the child is not larger: return False
        - If this node has a right child and we want to Turn Right
            - We ensure that the right child is smaller that the node and the parent
            - This ensures That we all nodes no left are strictly LARGER
        
        AND the results of calling leftHelper(on left child) and RightHelper(on Right Child)
    
    - Right Helper takes in node and parent node
        - If this node is none, return True cause this is a leaf
        - If this node has a right child and we want to keep going right, 
            - We just check if the node is smaller, 
            - Keeping all right values small
        
        - If this node has a left child, and we want to turn left, 
            - We have to ensure that it is larger than the node's value
            - BUUUUTTTT it has to be smaller than the grandparent
            - Keeping all nodes on the right side, smaller than root
        AND the results of calling leftHelper(on left child) and RightHelper(on Right Child)
        
    - Return the return values of leftHelper(root.left) and RightHelper(root.right)


"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lower, upper): 
            if not node:
                return True
            
            if not (node.val > lower and node.val < upper):
                return False
            
            return (valid(node.left, lower, node.val) and 
                    valid(node.right, node.val, upper))
        
        return valid(root, -float("inf"), float("inf"))











