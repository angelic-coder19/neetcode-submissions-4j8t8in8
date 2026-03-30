# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None

        # Reverse second half
        curr = second_half
        prev = None
        while curr: 
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        second_half = prev

        # Merge first half with reversed second half
        first = head
        second = second_half
        while second:
            first_next, second_next = first.next, second.next
            second.next = first.next 
            first.next = second
            first = first_next
            second = second_next
        