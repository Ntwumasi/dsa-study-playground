class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, low=-math.inf, high=math.inf):
            #base cases for bst.
            if not node:
                return True
            if not (low < node.val < high):
                return False
            #now that we have the base cases set up for dfs lets call the dfs recursive function
            #we are going to check left
            # we are going to check right
            return dfs(node.left,low,node.val) and
                    dfs(node.right,node.val,high)
        
        return dfs(root)