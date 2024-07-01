class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Determine the lengths of word1 and word2
        m = len(word1)
        n = len(word2)
        
        # Initialize a 2D list (dp table) with dimensions (m + 1) x (n + 1)
        # dp[i][j] will store the minimum number of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases:
        # If word2 is empty, the only operation is to delete all characters of word1
        for i in range(1, m + 1):
            dp[i][0] = i
        
        # If word1 is empty, the only operation is to insert all characters of word2
        for j in range(1, n + 1):
            dp[0][j] = j
        
        # Fill the dp table for the remaining cases
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters of word1 and word2 match at current positions
                if word1[i - 1] == word2[j - 1]:
                    # No additional operation is needed, inherit the value from the diagonal
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose the minimum of three possible operations (replace, delete, insert) + 1
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        # Return the minimum number of operations to convert word1 to word2
        return dp[m][n]