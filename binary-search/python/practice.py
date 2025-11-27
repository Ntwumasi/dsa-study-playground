"""
Binary Tree Practice Problems

A collection of common binary tree problems demonstrating DFS patterns:
1. Maximum Depth (LeetCode 104)
2. Invert Binary Tree (LeetCode 226)
3. Same Tree (LeetCode 100)
4. Symmetric Tree (LeetCode 101)

PATTERN: DFS Recursion on Trees
- Base case: handle None nodes
- Recursive case: process current node and recurse on children
- Combine results from subtrees

TIME COMPLEXITY: O(n) for all - visit each node once
SPACE COMPLEXITY: O(h) - recursion stack (h = height)
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# Problem 1: Maximum Depth of Binary Tree (LeetCode 104)
# =============================================================================

def max_depth(root: Optional[TreeNode]) -> int:
    """
    Find the maximum depth (number of nodes on longest root-to-leaf path).

    Args:
        root: Root of binary tree

    Returns:
        Maximum depth (0 for empty tree)

    Visual:
            3
           / \
          9  20
            /  \
           15   7

    Depth = 3 (path: 3 → 20 → 15 or 3 → 20 → 7)

    Recurrence:
    - depth(None) = 0
    - depth(node) = 1 + max(depth(left), depth(right))
    """
    # Base case: empty tree has depth 0
    if not root:
        return 0

    # Recursive case: 1 (current) + max of children's depths
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# =============================================================================
# Problem 2: Invert Binary Tree (LeetCode 226)
# =============================================================================

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert a binary tree (mirror image).

    Swap left and right children at every node.

    Args:
        root: Root of binary tree

    Returns:
        Root of inverted tree

    Visual:
        Before:         After:
            4              4
           / \            / \
          2   7    →     7   2
         / \ / \        / \ / \
        1  3 6  9      9  6 3  1
    """
    # Base case: nothing to invert
    if not root:
        return None

    # Recursively invert subtrees
    left = invert_tree(root.left)
    right = invert_tree(root.right)

    # Swap children
    root.left = right
    root.right = left

    return root


# =============================================================================
# Problem 3: Same Tree (LeetCode 100)
# =============================================================================

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are identical.

    Two trees are the same if they have:
    - Same structure
    - Same node values

    Args:
        p: Root of first tree
        q: Root of second tree

    Returns:
        True if trees are identical

    Visual:
        Tree 1:    Tree 2:
          1          1
         / \        / \
        2   3      2   3
        → Same!

        Tree 1:    Tree 2:
          1          1
         /            \
        2              2
        → Different! (structure differs)
    """
    # Both empty → same
    if not p and not q:
        return True

    # One empty, one not → different
    if not p or not q:
        return False

    # Both non-empty: check value and recurse
    if p.val != q.val:
        return False

    # Recursively check both subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# =============================================================================
# Problem 4: Symmetric Tree (LeetCode 101)
# =============================================================================

def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Check if a binary tree is symmetric (mirror of itself).

    Args:
        root: Root of binary tree

    Returns:
        True if symmetric

    Visual:
        Symmetric:          Not symmetric:
            1                   1
           / \                 / \
          2   2               2   2
         / \ / \               \   \
        3  4 4  3               3   3
    """
    def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        """Check if two trees are mirror images of each other."""
        # Both empty → mirror
        if not t1 and not t2:
            return True

        # One empty → not mirror
        if not t1 or not t2:
            return False

        # Check value and mirror relationship
        if t1.val != t2.val:
            return False

        # Mirror check: t1's left matches t2's right, and vice versa
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    # Empty tree is symmetric
    if not root:
        return True

    return is_mirror(root.left, root.right)


# =============================================================================
# Test Cases
# =============================================================================

if __name__ == "__main__":
    # Build test tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Test max depth
    print("Max depth:", max_depth(root))  # 3

    # Test invert
    #     3              3
    #    / \    →       / \
    #   9  20          20   9
    #     /  \        /  \
    #    15   7      7   15
    inverted = invert_tree(root)
    print("Inverted root left:", inverted.left.val)   # 20
    print("Inverted root right:", inverted.right.val) # 9

    # Test same tree
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree3 = TreeNode(1, TreeNode(2), None)
    print("Same tree (1,2):", is_same_tree(tree1, tree2))  # True
    print("Same tree (1,3):", is_same_tree(tree1, tree3))  # False

    # Test symmetric
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    sym_root = TreeNode(1)
    sym_root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    sym_root.right = TreeNode(2, TreeNode(4), TreeNode(3))
    print("Is symmetric:", is_symmetric(sym_root))  # True

    """
    DFS PATTERN SUMMARY:

    Most tree problems follow this template:

    def solve(root):
        # Base case
        if not root:
            return base_value

        # Recursively solve for subtrees
        left_result = solve(root.left)
        right_result = solve(root.right)

        # Combine results
        return combine(root.val, left_result, right_result)

    The key is identifying:
    1. What's the base case? (usually empty tree)
    2. What do we compute for each node?
    3. How do we combine left and right results?
    """
