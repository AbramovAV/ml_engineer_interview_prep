class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        for i in range(m):
            row = [0] * n
            matrix.append(row)
        matrix[0][0]=1
        for i in range(m):
            for j in range(n):
                if i:
                    matrix[i][j] += matrix[i-1][j]
                if j:
                    matrix[i][j] += matrix[i][j-1]
        return matrix[m-1][n-1]