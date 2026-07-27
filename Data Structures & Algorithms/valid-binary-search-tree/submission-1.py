# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ##left subtree contains only nodes with less than nodes key
        ##right subtree contains only nodes greate than nodes key
        ##every node must fall btw a range left < parent , right > parent
        initial_range = [float("-inf"),float('inf')]
        def dfs(root,left,right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            
            return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
        
        return dfs(root, float("-inf"), float("inf"))

