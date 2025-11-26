# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
# we want to eliminate negative values
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

             # Path that goes through this node (could be split into two branches)
            current_sum = node.val + left + right
            
            # Update global max
            max_sum = max(max_sum, current_sum)
            
            # Return the best one-side path to parent
            return node.val + max(left, right)
        
        dfs(root)
        return max_sum