"""
    Problem link :- "https://www.interviewbit.com/problems/max-non-negative-subarray/"
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        last_subset = list()
        last_sum = -1

        this_sum = -1
        this_sub_arr = list()

        for i in A:
            if i >= 0:
                this_sum += i
                this_sub_arr.append(i)

            else:
                if this_sum > last_sum:
                    last_sum = this_sum
                    last_subset = this_sub_arr

                elif this_sum == last_sum:
                    if len(this_sub_arr) > len(last_subset):
                        last_sum = this_sum
                        last_subset = this_sub_arr

                this_sum = 0
                this_sub_arr = list()

            if this_sum > last_sum:
                last_sum = this_sum
                last_subset = this_sub_arr

            elif this_sum == last_sum:
                if len(this_sub_arr) > len(last_subset):
                    last_sum = this_sum
                    last_subset = this_sub_arr

        return last_subset


if __name__ == '__main__':
    sol = Solution()
    # test_arr = [1, 2, 5, -7, 2, 3]
    test_arr = [756898537, -1973594324, -2038664370, -184803526, 1424268980]
    print(sol.maxset(test_arr))
