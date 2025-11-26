# Python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        # Define the depth-first search
        def dfs(root):
            if root is None:
                return 0
            # If only one of child is non-null, then go into that recursion.
            if root.left is None:
                return 1 + dfs(root.right)
            elif root.right is None:
                return 1 + dfs(root.left)
            # Both children are non-null, hence call for both children.
            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)

# Test case 1: Empty tree
root1 = None

# Test case 2: Single node
root2 = TreeNode(1)

# Test case 3: Root with one child
root3 = TreeNode(1)
root3.left = TreeNode(2)

# Test case 4: Balanced binary tree
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.right.right = TreeNode(5)

# Run tests
sol = Solution()
print("Test 1 (Empty):", sol.minDepth(root1))  # ➜ 0
print("Test 2 (Single):", sol.minDepth(root2))  # ➜ 1
print("Test 3 (One child):", sol.minDepth(root3))  # ➜ 2
print("Test 4 (Balanced):", sol.minDepth(root4))  # ➜ 2