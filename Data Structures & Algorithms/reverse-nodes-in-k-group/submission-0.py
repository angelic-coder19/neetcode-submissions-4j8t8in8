# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        last = curr = dummy
        counter, ptr = 0, head

        while ptr: 
            curr.next = ptr
            curr = curr.next
            counter += 1
            ptr = ptr.next

            if counter == k:
                end = last.next
                
                prev, cur = None, end
                for _ in range(k):
                    next = cur.next 
                    cur.next = prev
                    prev = cur
                    cur = next

                last.next = prev
                last = curr = end
                counter = 0
                
        return dummy.next