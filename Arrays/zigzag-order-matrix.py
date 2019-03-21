import math


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0 for x in range(A)] for y in range(A)]
        matrix[1][2] = 67
        n = 1

        for i in range(A):
            if (i + 1) / 2 == math.floor((i + 1) / 2):
                flag = True
            else:
                flag = False

            if flag:
                for j in reversed(range(A)):
                    matrix[i][j] = n
                    n += 1

            else:
                for j in range(A):
                    matrix[i][j] = n
                    n += 1

            if n > A * A:
                break

        return matrix


if __name__ == '__main__':
    sol = Solution()
    n = 3
    arr = sol.generateMatrix(n)

    for i in range(n):
        for j in range(n):
            print(arr[i][j], ', ', end='')

        print('\n')
