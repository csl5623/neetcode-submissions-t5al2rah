# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head

        while node:
            stack.append(node)
            node = node.next
        
        l = 0
        r = len(stack) - 1

        while l < r:
            stack[l].next = stack[r]
            l+=1
            if l >=r:
                break
            stack[r].next = stack[l]
            r-=1
        stack[l].next = None
        
            
