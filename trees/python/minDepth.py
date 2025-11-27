"""
Minimum Depth of Binary Tree (LeetCode 111)

PATTERN: DFS/BFS - Find Shortest Path to Leaf
- Minimum depth is shortest path from root to any leaf
- A leaf is a node with no children
- Must handle nodes with only one child carefully

TIME COMPLEXITY: O(n) - visit each node
SPACE COMPLEXITY: O(h) for DFS, O(w) for BFS where w is max width

WHY THIS WORKS:
- We're looking for the closest leaf node
- DFS explores depth-first, tracks minimum
- BFS finds first leaf (optimal for this problem)
- Must not count single-child nodes as leaves
"""

from typing import Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find minimum depth of binary tree.

        Minimum depth is the number of nodes along the shortest path
        from root to the nearest leaf node.

        Args:
            root: Root of binary tree

        Returns:
            Minimum depth (0 for empty tree)

        Visual:
                3
               / \
              9  20
                /  \
               15   7

            Paths to leaves:
            - 3 -> 9 (depth 2) <- minimum!
            - 3 -> 20 -> 15 (depth 3)
            - 3 -> 20 -> 7 (depth 3)

            Answer: 2

        Edge case - single child:
                1
               /
              2

            Path: 1 -> 2 (depth 2)
            Note: Node 1 is NOT a leaf (it has a child)
            Answer: 2 (not 1!)
        """
        def dfs(node):
            if node is None:
                return 0

            # If only right child exists, go right
            if node.left is None:
                return 1 + dfs(node.right)

            # If only left child exists, go left
            if node.right is None:
                return 1 + dfs(node.left)

            # Both children exist - take minimum
            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)


def min_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    BFS approach - often more efficient for this problem.

    BFS finds the first leaf (closest to root) naturally.
    No need to explore entire tree.

    TIME: O(n) worst case, but often better
    SPACE: O(w) where w is max width of tree
    """
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # Check if this is a leaf
        if not node.left and not node.right:
            return depth  # First leaf found = minimum depth

        # Add children to queue
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


def min_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    """
    Iterative DFS using stack.

    Similar to recursive but explicit stack.
    """
    if not root:
        return 0

    stack = [(root, 1)]
    min_depth = float('inf')

    while stack:
        node, depth = stack.pop()

        # If leaf node, update minimum
        if not node.left and not node.right:
            min_depth = min(min_depth, depth)
            continue

        # Add children (no need to explore deeper than current min)
        if node.left and depth + 1 < min_depth:
            stack.append((node.left, depth + 1))
        if node.right and depth + 1 < min_depth:
            stack.append((node.right, depth + 1))

    return min_depth


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Empty tree
    root1 = None
    print(f"Empty tree: {sol.minDepth(root1)}")  # 0

    # Test case 2: Single node
    root2 = TreeNode(1)
    print(f"Single node: {sol.minDepth(root2)}")  # 1

    # Test case 3: Left-skewed tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    print(f"Left-skewed [1,2]: {sol.minDepth(root3)}")  # 2

    # Test case 4: Balanced tree
    root4 = TreeNode(3)
    root4.left = TreeNode(9)
    root4.right = TreeNode(20)
    root4.right.left = TreeNode(15)
    root4.right.right = TreeNode(7)
    print(f"Balanced tree: {sol.minDepth(root4)}")  # 2

    # Test case 5: Right-skewed (deep)
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    root5.right.right.right = TreeNode(4)
    print(f"Right-skewed: {sol.minDepth(root5)}")  # 4

    # BFS approach
    print(f"\nBFS approach: {min_depth_bfs(root4)}")  # 2

    """
    DFS vs BFS FOR MIN DEPTH:

    DFS:
    - Must explore entire tree to find minimum
    - Good when tree is balanced
    - O(n) time always

    BFS:
    - Stops as soon as first leaf is found
    - Better for skewed trees with shallow leaves
    - Can be O(1) in best case (root is leaf)

    COMMON MISTAKE - LEAF DEFINITION:

    A leaf has NO children (both left and right are None).

    Wrong: Treating single-child nodes as leaves
        1
       /
      2

    If we return min(left_depth, right_depth) at node 1:
    - left_depth = 1 + depth(2) = 2
    - right_depth = 1 + depth(None) = 1  <- WRONG!

    Node 1 is NOT a leaf, so we can't count depth 1.
    We must continue to node 2 (the actual leaf).

    RELATED PROBLEMS:
    - Maximum Depth of Binary Tree (LeetCode 104) - simpler
    - Balanced Binary Tree (LeetCode 110) - compare depths
    - Path Sum (LeetCode 112) - find path with target sum
    """
