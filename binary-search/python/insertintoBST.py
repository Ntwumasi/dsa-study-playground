"""
Insert into a Binary Search Tree (LeetCode 701)

PATTERN: BST Property + Recursion
- BST property: left < root < right
- To insert, traverse down using BST property
- Insert at the first empty (None) spot

TIME COMPLEXITY: O(h) where h is tree height
- Best case (balanced): O(log n)
- Worst case (skewed): O(n)

SPACE COMPLEXITY: O(h) for recursion stack

WHY THIS WORKS:
- BST property tells us exactly which direction to go
- We keep going until we find an empty spot
- Insert there to maintain BST property
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Insert a value into a BST and return the root.

    Args:
        root: Root of the BST (can be None for empty tree)
        val: Value to insert

    Returns:
        Root of the BST after insertion

    Visual:
        Insert 5 into:
              4
             / \
            2   7
           / \
          1   3

        Step 1: 5 > 4, go right to 7
        Step 2: 5 < 7, go left (None)
        Step 3: Insert 5 as left child of 7

        Result:
              4
             / \
            2   7
           / \ /
          1  3 5
    """
    # Base case: found empty spot, create new node
    if not root:
        return TreeNode(val)

    # Recursive case: navigate using BST property
    if val < root.val:
        # Value belongs in left subtree
        root.left = insert_into_bst(root.left, val)
    else:
        # Value belongs in right subtree (assuming no duplicates)
        root.right = insert_into_bst(root.right, val)

    return root


def insert_into_bst_iterative(root: TreeNode, val: int) -> TreeNode:
    """
    Iterative version of BST insertion.

    More space-efficient: O(1) instead of O(h)
    """
    new_node = TreeNode(val)

    # Handle empty tree
    if not root:
        return new_node

    # Find the correct position
    current = root
    while True:
        if val < current.val:
            # Go left
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            # Go right
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root


def inorder_traversal(root: TreeNode) -> list[int]:
    """Helper function to verify BST property (should be sorted)."""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Test cases
if __name__ == "__main__":
    # Build initial BST
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print("Before insertion:", inorder_traversal(root))  # [1, 2, 3, 4, 7]

    # Insert 5
    root = insert_into_bst(root, 5)
    print("After inserting 5:", inorder_traversal(root))  # [1, 2, 3, 4, 5, 7]

    # Insert 6
    root = insert_into_bst_iterative(root, 6)
    print("After inserting 6:", inorder_traversal(root))  # [1, 2, 3, 4, 5, 6, 7]

    """
    BST PROPERTY RECAP:

    For every node in a BST:
    - All values in left subtree < node value
    - All values in right subtree > node value

    This property allows:
    - O(log n) search (on average, for balanced trees)
    - O(log n) insert (on average)
    - Inorder traversal gives sorted order

    Inorder traversal: Left → Root → Right
    Result is always sorted for a valid BST!
    """
