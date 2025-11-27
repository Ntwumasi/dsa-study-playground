"""
Flatten Binary Tree to Linked List (LeetCode 114)

PATTERN: DFS Pre-order with Pointer Manipulation
- Traverse tree in pre-order (root, left, right)
- Reconnect nodes as a right-skewed linked list

TIME COMPLEXITY: O(n) - visit each node once
SPACE COMPLEXITY: O(n) for the approach below (storing nodes)

Note: There's also an O(1) space Morris traversal solution.

WHY THIS WORKS:
- Pre-order traversal gives us the order we want
- We just need to reconnect the nodes in that order
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def flatten_binary_tree(root: Optional[TreeNode]) -> None:
    """
    Flatten binary tree to linked list IN-PLACE.

    The linked list uses the same TreeNode class:
    - 'right' pointer is the 'next' in linked list
    - 'left' pointer is always None

    Args:
        root: Root of binary tree (modified in-place)

    Visual:
        Before:
              1
             / \
            2   5
           / \   \
          3   4   6

        Pre-order: [1, 2, 3, 4, 5, 6]

        After:
        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
    """
    if not root:
        return

    # Step 1: Collect nodes in pre-order
    nodes = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        nodes.append(node)      # Pre-order: visit root first
        dfs(node.left)          # Then left subtree
        dfs(node.right)         # Then right subtree

    dfs(root)

    # Step 2: Reconnect nodes as linked list
    for i in range(1, len(nodes)):
        prev = nodes[i - 1]
        curr = nodes[i]
        prev.left = None        # Clear left pointer
        prev.right = curr       # Connect to next node


def flatten_recursive(root: Optional[TreeNode]) -> None:
    """
    O(1) space recursive solution (not counting call stack).

    Uses reverse pre-order (right, left, root) with a 'prev' pointer.
    """
    prev = None

    def dfs(node: Optional[TreeNode]) -> None:
        nonlocal prev

        if not node:
            return

        # Process right first, then left (reverse pre-order)
        dfs(node.right)
        dfs(node.left)

        # Now process current node
        node.right = prev
        node.left = None
        prev = node

    dfs(root)


def flatten_iterative(root: Optional[TreeNode]) -> None:
    """
    O(1) space iterative solution.

    Uses the Morris traversal-like approach.
    """
    current = root

    while current:
        if current.left:
            # Find rightmost node in left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right

            # Connect it to current's right subtree
            rightmost.right = current.right

            # Move left subtree to right
            current.right = current.left
            current.left = None

        # Move to next node
        current = current.right


def tree_to_list(root: Optional[TreeNode]) -> list[int]:
    """Helper to convert flattened tree to list for testing."""
    result = []
    current = root
    while current:
        result.append(current.val)
        current = current.right
    return result


# Test cases
if __name__ == "__main__":
    # Build test tree
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   6
    def build_tree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        return root

    # Test first approach
    root1 = build_tree()
    flatten_binary_tree(root1)
    print("Approach 1:", tree_to_list(root1))  # [1, 2, 3, 4, 5, 6]

    # Test recursive approach
    root2 = build_tree()
    flatten_recursive(root2)
    print("Approach 2:", tree_to_list(root2))  # [1, 2, 3, 4, 5, 6]

    # Test iterative approach
    root3 = build_tree()
    flatten_iterative(root3)
    print("Approach 3:", tree_to_list(root3))  # [1, 2, 3, 4, 5, 6]

    """
    PRE-ORDER TRAVERSAL REVIEW:

    Order: Root → Left → Right

    For tree:
          1
         / \
        2   3

    Pre-order: [1, 2, 3]

    Why pre-order for flattening?
    - Root comes first
    - Then entire left subtree
    - Then entire right subtree

    This matches the structure of our flattened list!
    """
