"""
Problem like: -https://www.interviewbit.com/problems/spiral-order-matrix-ii/
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        mat = [[0] * A for i in range(A)]
        steps, curr = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        i = j = k = 0  # current position (i, j), and current ring k
        tmp = 1  # current element

        while tmp <= A * A:
            mat[i][j] = tmp
            tmp += 1
            step_x, step_y = steps[curr]
            i, j = i + step_x, j + step_y

            # check does current position match any corner or current ring (k)
            curr += (curr == 0 and j == A - 1 - k) + (curr == 1 and i == A - 1 - k) + (curr == 2 and j == k) + (
                    curr == 3 and i == k)

            if curr == 4:
                i, j, k, curr = i + 1, j + 1, k + 1, 0

        return mat


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(4))
