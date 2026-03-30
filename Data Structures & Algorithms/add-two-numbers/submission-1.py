# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        ptr1, ptr2 = l1, l2
        carry = 0
        while ptr1 and ptr2:
            sum = carry + ptr2.val + ptr1.val
            digit = ListNode(sum % 10)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            ans.next = digit
            ans = ans.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        while ptr1:
            sum = carry + ptr1.val
            digit = ListNode(sum % 10)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            ans.next = digit
            ans = ans.next
            ptr1 = ptr1.next
        
        while ptr2:
            sum = carry + ptr2.val
            digit = ListNode(sum % 10)
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            ans.next = digit
            ans = ans.next
            ptr2 = ptr2.next
        
        if carry == 1:
            digit = ListNode(carry)
            ans.next = digit
            ans = ans.next
        
        return dummy.next
