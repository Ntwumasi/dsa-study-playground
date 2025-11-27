"""
Binary Tree Maximum Path Sum (LeetCode 124)

PATTERN: DFS with Global Maximum Tracking
- For each node, calculate max path sum through that node
- A path can go left-root-right (split) or continue up
- Track global maximum across all possible paths

TIME COMPLEXITY: O(n) - visit each node once
SPACE COMPLEXITY: O(h) - recursion stack (h = tree height)

WHY THIS WORKS:
- At each node, we have two choices:
  1. The path splits here (left + node + right) - potential global max
  2. The path continues upward (node + max(left, right)) - return value
- We track the global max separately from what we return

KEY INSIGHT:
- Return value: best single-path sum from node upward
- Global max: considers split paths that can't extend further
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum path sum in a binary tree.

        A path is any sequence of nodes connected by edges.
        Path doesn't need to pass through root.
        Each node appears at most once in the path.

        Args:
            root: Root of binary tree

        Returns:
            Maximum path sum

        Visual:
               -10
               / \
              9  20
                /  \
               15   7

        Possible paths and their sums:
        - [15] = 15
        - [9] = 9
        - [15, 20, 7] = 42  <- Maximum!
        - [15, 20, -10, 9] = 34
        - etc.

        Answer: 42 (path 15 → 20 → 7)
        """
        max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            """
            Returns the maximum sum of a path starting from this node
            going downward (only one direction - can't split).
            """
            nonlocal max_sum

            if not node:
                return 0

            # Get max contribution from left and right subtrees
            # Use max(0, ...) to ignore negative contributions
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Calculate path sum IF we split at this node
            # (path goes left -> node -> right)
            current_sum = node.val + left + right

            # Update global maximum with split path
            max_sum = max(max_sum, current_sum)

            # Return max single path to parent
            # (can only go one direction when continuing up)
            return node.val + max(left, right)

        dfs(root)
        return max_sum


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Simple tree
    #   1
    #  / \
    # 2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(sol.max_path_sum(root1))  # 6 (path: 2 → 1 → 3)

    # Example 2: With negative
    #    -10
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(sol.max_path_sum(root2))  # 42 (path: 15 → 20 → 7)

    # Example 3: All negative
    #   -3
    root3 = TreeNode(-3)
    print(sol.max_path_sum(root3))  # -3 (must include at least one node)

    # Example 4: Single path is best
    #     1
    #    /
    #   2
    #  /
    # 3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    print(sol.max_path_sum(root4))  # 6 (path: 3 → 2 → 1)

    """
    UNDERSTANDING THE TWO VALUES:

    At each node, we compute two things:

    1. current_sum = node.val + left + right
       - This is the sum if the path SPLITS at this node
       - We use this to update global maximum
       - This path can't extend further up (would create a branch)

    2. Return value = node.val + max(left, right)
       - This is what we can contribute to parent
       - Only ONE direction (left or right, not both)
       - This allows the path to potentially extend upward

    Visual:
            A
           / \
          B   C

    If path splits at A: B-A-C (sum = B + A + C)
    If path continues through A: either B-A-parent or C-A-parent
    """
