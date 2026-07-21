# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
U:
    Input: head of a linked list
    Output: The head of the new linked list reversed
M:
    - Linked Lists, - Dummy nodes 
P:
    - Create a new dummy node and declare a pointer
    - Set a curr pointer to point to the dummy node
    - Set a pointer prev to point to the head of the original
    - While the prev pointer is not NULL
        - 
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev





