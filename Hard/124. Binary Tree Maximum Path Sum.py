# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')  # Initialize the global maximum path sum

        def dfs(node):
            nonlocal global_max
            if not node:
                return 0  # Return 0 if the node is None

            # Recursively calculate the maximum path sum for the left and right subtrees
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Calculate the path sum that passes through the current node
            current_path = node.val + left_gain + right_gain

            # Update the global maximum path sum
            global_max = max(global_max, current_path)

            # Return the maximum gain that can be included in the path from the current node
            return node.val + max(left_gain, right_gain)

        # Start the DFS from the root
        dfs(root)

        # Return the global maximum path sum found
        return global_max
