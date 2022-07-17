class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        target_rows, target_columns = set(), set()
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if column == 0:
                    if not i in target_rows:
                        target_rows.add(i)
                    if not j in target_columns:
                        target_columns.add(j)
        
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if i in target_rows or j in target_columns:
                    matrix[i][j] = 0

        return matrix

