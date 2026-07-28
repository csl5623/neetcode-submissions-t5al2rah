# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        tree_list = list()
        count = 0
        k_noth  = None
        def dfs(root):
            nonlocal count, k_noth
            if not root:
                return 
            
            dfs(root.left)
            if count == k:
                return 
            count +=1
            if count == k:
                k_noth = root.val
                return 
            dfs(root.right)
        
        dfs(root)
        return k_noth

        