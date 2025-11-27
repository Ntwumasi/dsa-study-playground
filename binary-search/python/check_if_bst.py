"""
Validate Binary Search Tree (LeetCode 98)

PATTERN: DFS with Range Validation
- Each node must be within a valid range (low, high)
- As we go left, update upper bound to current node
- As we go right, update lower bound to current node

TIME COMPLEXITY: O(n) - visit each node once
SPACE COMPLEXITY: O(h) - recursion stack depth (h = tree height)

WHY THIS WORKS:
- BST property: left < root < right
- But this must hold for ALL ancestors, not just parent
- By passing down valid range, we ensure global BST property
"""

import math
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is a valid BST.

        Args:
            root: Root of binary tree

        Returns:
            True if valid BST, False otherwise

        Visual:
              5
             / \
            1   7
               / \
              4   8

        Is this a valid BST? NO!
        - 5 > 1 ✓ (left child smaller)
        - 5 < 7 ✓ (right child larger)
        - But 4 is in right subtree of 5, yet 4 < 5 ✗

        The value 4 violates the BST property because it's in
        the right subtree of 5 but is less than 5.
        """
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            # Base case: empty tree is valid
            if not node:
                return True

            # Check if current node violates range constraint
            if not (low < node.val < high):
                return False

            # Recursively check subtrees with updated bounds:
            # - Left subtree: all values must be < node.val
            # - Right subtree: all values must be > node.val
            return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))

        # Start with infinite bounds
        return dfs(root, -math.inf, math.inf)


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """
    Alternative: Use inorder traversal.

    BST property: inorder traversal should give sorted order.
    If current value <= previous value, it's not a valid BST.
    """
    prev = -math.inf

    def inorder(node: Optional[TreeNode]) -> bool:
        nonlocal prev

        if not node:
            return True

        # Check left subtree
        if not inorder(node.left):
            return False

        # Check current node (must be > previous)
        if node.val <= prev:
            return False
        prev = node.val

        # Check right subtree
        return inorder(node.right)

    return inorder(root)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Valid BST
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(sol.is_valid_bst(root1))  # True

    # Example 2: Invalid BST
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    print(sol.is_valid_bst(root2))  # False (3 and 4 violate BST)

    # Example 3: Tricky case - valid local but invalid global
    #     5
    #    / \
    #   1   7
    #      / \
    #     4   8
    root3 = TreeNode(5)
    root3.left = TreeNode(1)
    root3.right = TreeNode(7)
    root3.right.left = TreeNode(4)  # 4 < 5 but in right subtree!
    root3.right.right = TreeNode(8)
    print(sol.is_valid_bst(root3))  # False

    # Test inorder approach
    print(is_valid_bst_inorder(root1))  # True
    print(is_valid_bst_inorder(root2))  # False

    """
    COMMON MISTAKE:

    Only checking node.left.val < node.val < node.right.val is NOT enough!

    Example:
          5
         / \
        1   7
           /
          4    <- 4 < 5, but 4 is in right subtree of 5!

    This is why we need to pass down the valid RANGE to each node,
    not just compare with immediate parent.
    """
