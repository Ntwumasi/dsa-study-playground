# Trees

## When to Use
- Hierarchical data
- Recursive problems
- Search operations (BST)
- Path finding

## Visual

### Binary Tree Structure
```
        ┌───┐
        │ 1 │         ← root
        └─┬─┘
       ┌──┴──┐
     ┌─┴─┐ ┌─┴─┐
     │ 2 │ │ 3 │      ← children
     └─┬─┘ └─┬─┘
    ┌──┴──┐  └──┐
  ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
  │ 4 │ │ 5 │ │ 6 │   ← leaves
  └───┘ └───┘ └───┘
```

### Traversal Orders
```
Tree:       1
           / \
          2   3
         / \
        4   5

In-order (Left, Root, Right):   4, 2, 5, 1, 3
Pre-order (Root, Left, Right):  1, 2, 4, 5, 3
Post-order (Left, Right, Root): 4, 5, 2, 3, 1
Level-order (BFS):              1, 2, 3, 4, 5
```

### Binary Search Tree (BST)
```
        ┌───┐
        │ 8 │
        └─┬─┘
       ┌──┴──┐
     ┌─┴─┐ ┌─┴─┐
     │ 3 │ │10 │
     └─┬─┘ └─┬─┘
    ┌──┴──┐  └──┐
  ┌─┴─┐ ┌─┴─┐ ┌─┴─┐
  │ 1 │ │ 6 │ │14 │
  └───┘ └───┘ └───┘

Property: left < root < right (for all nodes)

Search for 6:
8 → 6 < 8, go left
3 → 6 > 3, go right
6 → Found! ✓

O(log n) average, O(n) worst
```

### Lowest Common Ancestor
```
        ┌───┐
        │ 3 │ ← LCA of 5 and 1
        └─┬─┘
       ┌──┴──┐
     ┌─┴─┐ ┌─┴─┐
     │ 5 │ │ 1 │
     └─┬─┘ └─┬─┘
    ┌──┴──┐ ┌┴─┐
  ┌─┴─┐ ┌─┴─┴─┐┌─┴─┐
  │ 6 │ │ 2 ││ 0 ││ 8 │
  └───┘ └───┘└───┘└───┘
```

## Template

### Python
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Traversals
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# BFS (Level-order)
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Max depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Lowest Common Ancestor
def lca(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    return left or right
```

### TypeScript
```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

// DFS Traversals
function inorder(root: TreeNode | null): number[] {
  if (!root) return [];
  return [...inorder(root.left), root.val, ...inorder(root.right)];
}

function preorder(root: TreeNode | null): number[] {
  if (!root) return [];
  return [root.val, ...preorder(root.left), ...preorder(root.right)];
}

function postorder(root: TreeNode | null): number[] {
  if (!root) return [];
  return [...postorder(root.left), ...postorder(root.right), root.val];
}

// BFS (Level-order)
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];
  const result: number[][] = [];
  const queue: TreeNode[] = [root];

  while (queue.length) {
    const level: number[] = [];
    const size = queue.length;

    for (let i = 0; i < size; i++) {
      const node = queue.shift()!;
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    result.push(level);
  }

  return result;
}

// Max depth
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

## Complexity
- **DFS Traversal:** O(n) time, O(h) space (h = height)
- **BFS Traversal:** O(n) time, O(w) space (w = max width)
- **BST Search:** O(log n) average, O(n) worst

## Common Problems
- [x] Maximum Depth
- [x] Lowest Common Ancestor
- [x] Flatten Binary Tree
- [ ] Validate BST
- [ ] Invert Binary Tree
- [ ] Path Sum
- [ ] Serialize/Deserialize
