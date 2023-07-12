class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up_idx = 0
        low_idx = len(matrix)
        left_idx = 0
        right_idx = len(matrix[0])
        output = []

        while True:
            if left_idx < right_idx:
                output.extend(matrix[up_idx][left_idx:right_idx])
            else:
                break

            up_idx += 1
            if up_idx < low_idx:
                output.extend([matrix[i][right_idx-1] for i in range(up_idx, low_idx)])
            else:
                break

            right_idx -= 1
            if left_idx < right_idx:
                output.extend(matrix[low_idx-1][left_idx:right_idx][::-1])
            else:
                break
            low_idx -= 1

            if up_idx < low_idx:
                output.extend([matrix[i][left_idx] for i in range(low_idx-1, up_idx-1, -1)])
            else:
                break
            left_idx += 1
        return output