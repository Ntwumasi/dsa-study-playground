"""
Flatten Binary Tree to Linked List (LeetCode 114)

PATTERN: Tree Traversal - Pre-order to Linked List
- Traverse tree in pre-order (root, left, right)
- Rearrange nodes into a right-skewed linked list
- Each node's left becomes None, right points to next pre-order node

TIME COMPLEXITY: O(n) - visit each node once
SPACE COMPLEXITY: O(n) for array approach, O(h) for recursive stack

WHY THIS WORKS:
- Pre-order traversal visits nodes in the exact order we want
- We collect nodes, then rewire their pointers
- Result is a "linked list" using only right pointers
"""

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten binary tree to linked list in-place.

        Do not return anything, modify root in-place instead.

        Args:
            root: Root of binary tree

        Visual:
            Input:
                    1
                   / \
                  2   5
                 / \   \
                3   4   6

            Pre-order: [1, 2, 3, 4, 5, 6]

            Output:
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

        Step-by-step rewiring:
            nodes = [1, 2, 3, 4, 5, 6]

            i=1: nodes[0].left=None, nodes[0].right=nodes[1]
                 1.left=None, 1.right=2

            i=2: nodes[1].left=None, nodes[1].right=nodes[2]
                 2.left=None, 2.right=3

            ... and so on
        """
        if not root:
            return

        # Collect nodes in pre-order
        nodes = []

        def preorder(node):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # Rewire nodes: each node's left=None, right=next node
        for i in range(1, len(nodes)):
            prev = nodes[i - 1]
            curr = nodes[i]
            prev.left = None
            prev.right = curr


def flatten_morris(root: Optional[TreeNode]) -> None:
    """
    Alternative: O(1) space using Morris-like traversal.

    For each node, find the rightmost node of its left subtree
    and connect it to the right child.
    """
    current = root

    while current:
        if current.left:
            # Find rightmost node in left subtree
            rightmost = current.left
            while rightmost.right:
                rightmost = rightmost.right

            # Connect rightmost to current's right child
            rightmost.right = current.right

            # Move left subtree to right
            current.right = current.left
            current.left = None

        # Move to next node
        current = current.right


def flatten_recursive(root: Optional[TreeNode]) -> None:
    """
    Alternative: Recursive approach with reverse pre-order.

    Process right, left, root (reverse pre-order).
    Use a global 'prev' to track the previously processed node.
    """
    prev = None

    def helper(node):
        nonlocal prev
        if not node:
            return

        # Process right subtree first
        helper(node.right)
        # Then left subtree
        helper(node.left)

        # Now process current node
        node.right = prev
        node.left = None
        prev = node

    helper(root)


# Helper functions
def create_tree_from_list(values):
    """Create binary tree from level-order list."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def print_flattened(root):
    """Print flattened tree (linked list)."""
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = create_tree_from_list([1, 2, 5, 3, 4, None, 6])
    sol.flatten(root1)
    print(f"[1,2,5,3,4,null,6] flattened: {print_flattened(root1)}")
    # [1, 2, 3, 4, 5, 6]

    # Example 2: Empty tree
    sol.flatten(None)
    print("[] flattened: []")

    # Example 3: Single node
    root3 = TreeNode(0)
    sol.flatten(root3)
    print(f"[0] flattened: {print_flattened(root3)}")  # [0]

    """
    THREE APPROACHES COMPARISON:

    1. Array approach (implemented above):
       - TIME: O(n), SPACE: O(n)
       - Simple: collect nodes, then rewire
       - Easy to understand

    2. Morris-like (O(1) space):
       - TIME: O(n), SPACE: O(1)
       - For each node with left child:
         a. Find rightmost of left subtree
         b. Connect it to current's right
         c. Move left subtree to right
       - No recursion or extra storage

    3. Reverse pre-order:
       - TIME: O(n), SPACE: O(h) for stack
       - Process right, left, root
       - Build list from end to start

    PRE-ORDER TRAVERSAL PATTERN:

    Pre-order: root -> left -> right
    - Process root first
    - Then entire left subtree
    - Then entire right subtree

    Used in:
    - Serialize/deserialize trees
    - Copy trees
    - Expression trees (prefix notation)

    MORRIS TRAVERSAL INSIGHT:
    The key insight is that in pre-order, left subtree nodes
    come before right subtree nodes. So we can safely move
    the left subtree to become the new right, then connect
    the original right at the end of the (former) left subtree.
    """
