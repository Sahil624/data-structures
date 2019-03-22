class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        diagonal_arr = [list() for i in range(2 * len(A) - 1)]

        for i in range(len(A)):
            for j in range(len(A)):
                diagonal_arr[i + j].append(A[i][j])

        return diagonal_arr


if __name__ == '__main__':
    sol = Solution()
    print(sol.diagonal([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]))
