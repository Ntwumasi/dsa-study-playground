# 1. call out my base cases
# 2. will create logic for val insertion
# 3. return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertBST(root,val):
    if not root:
        return TreeNode.val
    # above is the base case we need from step 1

    if val < root.val:
        root.left = insertBST(root.left, val)
    else:
        root.right = insertBST(root.right, val)

    # above we created the logic for the insertion of the val recursively 
    # 
    return root   