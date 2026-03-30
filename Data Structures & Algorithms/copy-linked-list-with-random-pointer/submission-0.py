"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originalToCopy = { None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            originalToCopy[cur] = copy
            cur = cur.next

        New = Node(0)
        new = New
        cur = head
        while cur:
            copy = originalToCopy[cur]
            copy.next = originalToCopy[cur.next]
            copy.random = originalToCopy[cur.random]
            cur = cur.next
            new.next = copy
            new = new.next
        
        return New.next
        
