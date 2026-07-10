class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        cur = head
        while cur:
            if cur in visited_nodes:
                return True
            visited_nodes.add(cur)
            cur = cur.next
        return False 