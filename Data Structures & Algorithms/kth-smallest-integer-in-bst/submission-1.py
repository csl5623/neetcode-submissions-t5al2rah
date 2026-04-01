# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        val = 0

        def dfs(root):
            nonlocal val,count
            if not root:
                return 0
            
            dfs(root.left)

            count -= 1
            if count == 0:
                val = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return val