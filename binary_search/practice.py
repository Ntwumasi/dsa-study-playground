# Given the root of a binary tree, return its maximum depth
# (i.e., the number of nodes along the longest path from the root down
# to the farthest leaf node).

#     3
#    / \
#   9  20
#      /  \
#     15   7

# Output: 3

# we will be using a dfs which is dfs and it uses the call stack behind the scene

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)

return 1 + max(left,right)

def invertTree(root):
    if not root:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left

return root

def isSameTree(p, q):
    # your logic here
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTree(p.left,p.right) and isSameTree(q.left,q.right)



   
def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    
    return isMirror(root.left, root.right) if root else True

