class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return  # If the matrix is empty, return immediately
        
        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns in the matrix
        zero_rows = set()  # Initialize a set to store indices of rows containing zeros
        zero_cols = set()  # Initialize a set to store indices of columns containing zeros
        
        # Identify rows and columns to be zeroed out
        for i in range(rows):  # Iterate through each row in the matrix
            for j in range(cols):  # Iterate through each column in the current row
                if matrix[i][j] == 0:  # If the current element is zero
                    zero_rows.add(i)  # Add the current row index to zero_rows set
                    zero_cols.add(j)  # Add the current column index to zero_cols set
        
        # Set zeros in the matrix based on zero_rows and zero_cols
        for i in range(rows):  # Iterate through each row in the matrix
            for j in range(cols):  # Iterate through each column in the current row
                if i in zero_rows or j in zero_cols:  # If either the current row or column index is in zero_rows or zero_cols
                    matrix[i][j] = 0  # Set the current element to zero