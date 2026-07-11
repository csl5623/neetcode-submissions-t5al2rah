# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        dummy = ListNode(0, prev)
        curr = dummy
        for i in range(n-1):
            curr = curr.next
        
        if curr:
            curr.next = curr.next.next
        
        new_prev = None
        curr = dummy.next
        while curr:
            temp = curr.next
            curr.next = new_prev
            new_prev =curr
            curr =temp
        return new_prev
        
           
        
