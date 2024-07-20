class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the root is None, return an empty list as there are no nodes to traverse.
        if not root:
            return []

        # Initialize the result list to hold the zigzag level order traversal.
        result = []
        # Initialize the queue with the root node to start the level order traversal.
        queue = deque([root])
        # Boolean variable to keep track of the direction of traversal. 
        # Start with left to right.
        left_to_right = True

        # Perform level order traversal until the queue is empty.
        while queue:
            # Get the number of nodes at the current level.
            level_size = len(queue)
            # Initialize a list to hold the values of nodes at the current level.
            level_values = []

            # Process all nodes at the current level.
            for _ in range(level_size):
                # Pop a node from the front of the queue.
                node = queue.popleft()

                # Depending on the current direction, append the node's value to the level_values list.
                if left_to_right:
                    level_values.append(node.val)  # Append at the end if left to right.
                else:
                    level_values.insert(0, node.val)  # Insert at the beginning if right to left.

                # Add the node's left child to the queue if it exists.
                if node.left:
                    queue.append(node.left)
                # Add the node's right child to the queue if it exists.
                if node.right:
                    queue.append(node.right)

            # After processing all nodes at the current level, add the level_values to the result.
            result.append(level_values)
            # Switch the direction for the next level.
            left_to_right = not left_to_right

        # Return the zigzag level order traversal.
        return result
