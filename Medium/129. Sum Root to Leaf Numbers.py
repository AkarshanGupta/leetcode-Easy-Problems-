class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the TreeNode with a value, and optional left and right children
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: TreeNode) -> int:
    # Helper function to perform DFS and calculate the sum of root-to-leaf numbers
    def dfs(node, current_number):
        # Base case: If the current node is None, return 0
        if not node:
            return 0
        
        # Update the current number by appending the current node's value
        current_number = current_number * 10 + node.val
        
        # If the current node is a leaf (no children), return the current number
        if not node.left and not node.right:
            return current_number
        
        # Recursively call dfs on the left subtree and accumulate the sum
        left_sum = dfs(node.left, current_number)
        
        # Recursively call dfs on the right subtree and accumulate the sum
        right_sum = dfs(node.right, current_number)
        
        # Return the sum of values from both left and right subtrees
        return left_sum + right_sum
    
    # Start the DFS traversal from the root with an initial current_number of 0
    return dfs(root, 0)
