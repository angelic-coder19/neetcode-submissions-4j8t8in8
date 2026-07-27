# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            # Iterate over each of the lits at this point 2 at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1,l2))

            # The goal is to keep combining the lists until there is only one left    
            lists = mergedLists
        
        return lists[0]   
        

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        ptr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            
            else: 
                ptr.next = l2
                l2 = l2.next
            
            ptr = ptr.next
        
        if l1: 
            ptr.next = l1
        
        if l2: 
            ptr.next = l2

        return dummy.next