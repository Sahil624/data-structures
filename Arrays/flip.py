"""
Problem link :- https://www.interviewbit.com/problems/flip/
"""


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        global_diff = current_diff = start = 0
        ans = None

        for i, a in enumerate(A):
            current_diff += (1 if a is '0' else -1)

            if current_diff < 0:
                start = i + 1
                current_diff = 0
                continue

            if current_diff > global_diff:
                global_diff = current_diff
                ans = [start, i]

        return [] if ans is None else (ans[0] + 1, ans[1] + 1)

    if __name__ == '__main__':
        sol = Solution()
        print(sol.flip('111'))
