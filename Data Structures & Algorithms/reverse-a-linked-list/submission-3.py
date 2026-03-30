# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Understanding:
    Input: Head of linked list
    Ouput: Head of reversed linked list

    Constraints:
    first Node has to be last, last node becomes first
    order has to be reversed 

    Edge cases:
    Only one node in linked list 
    Zero nodes in liked list 


Match:
    Linked lists, Two pointers

Planning:
    To swap the pointers of each of the nodes in the list
    initialize two pointers 
        curr to point at the head of the given list
        previous to point to nothing
    As long as curr exists:
        set a temporary variable (next) to point to curr's next value
        set curr's next pointer to prev
        set prev to point to curr
        set curr to point to next
    the head of the reversed linked list will be pointed to by prev

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