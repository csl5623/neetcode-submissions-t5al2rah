# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root,max_root):
            if not root:
                return 0
            
            res = 0
            if root.val >= max_root.val:
                max_root = root
                res =1
            
            res += dfs(root.left,max_root)
            res += dfs(root.right,max_root)

            return res
        return dfs(root,root)