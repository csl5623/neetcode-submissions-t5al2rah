# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        tree_list = list()

        def dfs(root):

            if not root:
                return False
            tree_list.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        if tree_list:
            sorted_list = sorted(tree_list)
            return sorted_list[k-1]

        