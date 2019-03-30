"""
    Find this problem at :- https://www.interviewbit.com/problems/hotel-bookings-possible/
"""

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort(), depart.sort()

        check_for_guest = checking_other_guest = current_guests = 0

        while check_for_guest < len(arrive):
            if checking_other_guest < len(depart) and depart[checking_other_guest] <= arrive[check_for_guest]:
                current_guests, checking_other_guest = current_guests - 1, checking_other_guest + 1

            else:
                current_guests, check_for_guest = current_guests + 1, check_for_guest + 1

            if current_guests > K:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.hotel([1, 3, 5], [2, 6, 8], 1))
