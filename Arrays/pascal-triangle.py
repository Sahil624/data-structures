"""
Problem Link :- https://www.interviewbit.com/problems/pascal-triangle/
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A > 0:
            triangle = [[1]]
            for i in range(A - 1):
                temp_arr = []
                for j in range(i + 2):
                    first_val = 0
                    if j - 1 >= 0:
                        first_val = triangle[i][j - 1]
                    second_val = 0
                    if j < len(triangle[i]):
                        second_val = triangle[i][j]

                    temp_arr.append(first_val + second_val)

                triangle.append(temp_arr)

            return triangle
        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(5))
