# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understanding:
    Input: root of binary tree
    Output: list of node values of nodes that can be seen from right side

    - There can be zero nodes in the tree
    - A left node can still be seen from the right side

Match:
    - BFS - Queue

Planning:
    - Declare a queque and results array
    - If the root is none return empty results array
    - While the queue is not empty:
        - Find length of deque 
        - Iterate as many times as there are nodes in the deque currently
            - Offload node from deque
            - If the index is equal to the last element at this level 
                - This means node is furthest to right so add val to result
            - Add left children if they exist 
            - Add right children if they exist
    - Return the results array
"""
from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, res = deque(), []

        if not root:
            return []
        
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()

                if (i + 1) == n:
                    res.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return res




