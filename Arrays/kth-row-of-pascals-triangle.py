class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row = [1]

        for i in range(A):
            row.append(row[i] * (A - i) // (i + 1))

        return row


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(3))
