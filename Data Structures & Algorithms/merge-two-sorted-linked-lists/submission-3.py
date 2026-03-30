# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Understanding:
    Input: heads of two sorted linked lists
    Output: the head a single linked list in order

    Constraints:   
    two lists may be of unequal length
    new list should be made up of nodes from two lists

    Edgecases:
    when linked lists are not of equal length -> sort them as long as they are the same length
    one list is empty while other is not -> return the other non-empty linked list
    both linked lists are empty -> return an empty linked list
    values in both lists are equal -> order doesn't matter


Match:
    Linked lists, dummy nodes, pointers

Planning:
    Declare a dummy node whose next pointer is nothing
    set a pointer to point to dummy node
    First part is handling equal length nodes
    set two pointers to the heads of both lists
    As long as BOTH pointers point to something:
        if the value in node2 is greater that value in node1
            extend dummy'next field to point to node1 
            advance node1's pointer to the next node
            advance dummy's pointer to the new node
        Do reverse if node2 is less than node1 
        
    Second part should handle remaining length of list
    if any of the pointers still exist:
        extend dummy's next pointer to point to that node

    return dummy's next node which should return the sorted list combined 


"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        l1, l2 = list1, list2
        while l1 and l2:
            if l2.val > l1.val:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
            else:
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
        
        if l1:
            ptr.next = l1
        elif l2:
            ptr.next = l2
        
        return dummy.next

    