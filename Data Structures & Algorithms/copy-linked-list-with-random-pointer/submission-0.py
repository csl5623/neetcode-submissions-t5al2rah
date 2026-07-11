
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        old_to_new = {None:None}

        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next
        
        ##2nd pass, make connections
        curr = head

        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
        
        ##return head of copy nodes
        return old_to_new[head]
        

        
