class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A) # Len of List

        l_min = [0] * n
        r_max = [0] * n

        l_min[0] = A[0]

        for i in range(1, n):
            l_min[i] = min(l_min[i - 1], A[i])

        r_max[n - 1] = A[n - 1]
        for j in range(n - 2, -1, -1):
            r_max[j] = max(A[j], r_max[j + 1])

        max_diff = -1
        i = j = 0

        while (i < n and j < n):
            if l_min[i] <= r_max[j]:
                max_diff = max(max_diff, j - i)
                j = j + 1
            else:
                i = i + 1


        return max_diff

if __name__ == '__main__':
    arr = [1, 3, 5, 6]
    sol = Solution()
    result = sol.maximumGap(arr)
    print('Result :- ', result)