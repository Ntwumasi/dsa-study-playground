# flattern a binary search tree to a linked list
# i believe the bst is not empty
# the linked list is singular
# i would create a variable to store an empty list
# then i would traverse the tree via pre-order to make
# sure i retrieve the elements then append this to the list
# i would then loop through the list and create my pointers for 
# the linked list
# i would need to take into consideration the base cases

def flatternBinaryTree(root):
    nodes = []
    def dfs(node):
        if not node:
            return
            # when you see a return with no additional context, we are just saying return nothing
        nodes.append(node)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
        # now we are going to create our linked list off of the nodes array
    for i in range(1,len(nodes)):
        prev = nodes[i - 1]
        curr = nodes[i]
        prev.left = None
        prev.right = curr


# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the
# path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

def getValues(root):
    # i really feel i can run a prefix sum on the list generated
    # or maybe i can use dynamic programing to figure out the sum like the max value but
    # that may not work, i need to get a working solution so lets try 
    values = []
    curr = 0
    def dfs(node):
        if not node:
            return 0
        values.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)

    for i in range(len(values)):
        curr += values[i]
        
    return curr
