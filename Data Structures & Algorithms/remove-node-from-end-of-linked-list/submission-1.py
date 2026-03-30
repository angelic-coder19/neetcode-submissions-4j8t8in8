# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        # First pass to find the length of the list
        N = 0
        curr = head
        while curr:
            curr = curr.next
            N += 1
        
        removeIndex = N - n
        dummy.next = head
        first = head
        while n > 0:
            first = first.next
            n -= 1
        
        second = dummy
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next
        