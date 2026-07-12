# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_node = ListNode(0)

        c1 = l1
        c2 = l2
        c3 = output_node
        carry = 0
        while c1 or c2 or carry:
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0
            output = val1 + val2 + carry
            carry = output // 10
            output = output % 10
            node = ListNode(output)
            c3.next = node
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
            c3 = c3.next

        return output_node.next
        
        
            
