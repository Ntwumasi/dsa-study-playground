"""
Lowest Common Ancestor of a Binary Tree (LeetCode 236)

PATTERN: DFS - Post-order with Result Propagation
- Search for both nodes p and q recursively
- LCA is the node where both subtrees return found results
- If current node is p or q, it could be the LCA

TIME COMPLEXITY: O(n) - visit each node at most once
SPACE COMPLEXITY: O(h) - recursion stack, h = tree height

WHY THIS WORKS:
- Post-order processes children before parent
- Each node reports whether p or q was found in its subtree
- When both sides report found, current node is the LCA
- If current node is p/q and one subtree has the other, current is LCA
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find lowest common ancestor of two nodes in a binary tree.

        The LCA is the lowest node that has both p and q as descendants
        (a node can be a descendant of itself).

        Args:
            root: Root of binary tree
            p: First target node
            q: Second target node

        Returns:
            The lowest common ancestor node

        Visual:
                    3
                   / \
                  5   1
                 /|   |\
                6 2   0 8
                 /|
                7 4

            LCA(5, 1) = 3  (5 in left subtree, 1 in right subtree)
            LCA(5, 4) = 5  (5 is ancestor of 4)
            LCA(6, 4) = 5  (both in left subtree, meet at 5)

        How recursion works for LCA(5, 1):
            - At node 3:
              - left = lowestCommonAncestor(5, 5, 1) -> returns 5
              - right = lowestCommonAncestor(1, 5, 1) -> returns 1
              - Both non-null -> return 3 (the LCA!)
        """
        # Base case: empty tree or found target node
        if not root or root == p or root == q:
            return root

        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides found something, current node is LCA
        if left and right:
            return root

        # Otherwise, return whichever side found something
        return left if left else right


def lca_with_parent(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Alternative: Using parent pointers (if available).

    If each node has a parent pointer, we can:
    1. Find all ancestors of p
    2. Walk up from q until we find a common ancestor

    TIME: O(h), SPACE: O(h)
    """
    # Simulate finding ancestors of p
    ancestors = set()

    # Walk up from p to root, collecting ancestors
    current = p
    while current:
        ancestors.add(current)
        current = getattr(current, 'parent', None)

    # Walk up from q until we find a common ancestor
    current = q
    while current:
        if current in ancestors:
            return current
        current = getattr(current, 'parent', None)

    return None


def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    For BST specifically (LeetCode 235).

    Use BST property: left < root < right

    TIME: O(h), SPACE: O(1) iterative or O(h) recursive
    """
    while root:
        if p.val < root.val and q.val < root.val:
            # Both in left subtree
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # Both in right subtree
            root = root.right
        else:
            # Split point found - this is the LCA
            return root

    return None


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Build test tree:
    #         3
    #        / \
    #       5   1
    #      /|   |\
    #     6 2   0 8
    #      /|
    #     7 4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p, q = root.left, root.right  # 5 and 1
    print(f"LCA(5, 1) = {sol.lowestCommonAncestor(root, p, q).val}")  # 3

    p, q = root.left, root.left.right.right  # 5 and 4
    print(f"LCA(5, 4) = {sol.lowestCommonAncestor(root, p, q).val}")  # 5

    p, q = root.left.left, root.left.right.right  # 6 and 4
    print(f"LCA(6, 4) = {sol.lowestCommonAncestor(root, p, q).val}")  # 5

    """
    LCA PROBLEM VARIATIONS:

    1. Binary Tree LCA (this problem - LeetCode 236):
       - General binary tree
       - Use DFS with result propagation
       - O(n) time, O(h) space

    2. BST LCA (LeetCode 235):
       - Use BST property for O(h) time
       - Compare values to decide direction

    3. LCA with Parent Pointers:
       - Walk up from both nodes
       - Find intersection of ancestor paths

    4. LCA for multiple nodes:
       - Extend algorithm to check for multiple targets

    RECURSION PATTERN EXPLAINED:

    The recursion returns:
    - The target node if found (p or q)
    - The LCA if both targets are found in subtrees
    - None if no target found in subtree

    Three cases at each node:
    1. Current node is p or q -> return it
    2. p and q in different subtrees -> current is LCA
    3. Both in same subtree -> propagate that subtree's result

    KEY INSIGHT:
    A node is the LCA if and only if:
    - One target is in its left subtree AND one in right subtree, OR
    - It IS one of the targets AND the other is in its subtree
    """
