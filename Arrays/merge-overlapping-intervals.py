# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals):

            class SortingKey(Interval):
                def __init__(self, interval):
                    super(SortingKey, self).__init__(interval.start, interval.end)

                def __lt__(self, other):
                    if self.start == other.start:
                        return self.end < other.end
                    return self.start < other.start

            intervals, ans = sorted(intervals, key=SortingKey), list()

            start, end = intervals[0].start, intervals[0].end

            for i in range(len(intervals)):
                end = max(end, intervals[i].end)

                if i == len(intervals) - 1 or intervals[i + 1].start > end:
                    ans.append(Interval(start, end))
                    if i != len(intervals) - 1:
                        start = intervals[i + 1].start
            return ans
        return []


if __name__ == '__main__':
    sol = Solution()
    interval = sol.merge([Interval(1, 3), Interval(8, 10), Interval(15, 18), Interval(2, 6)])

    for i in interval:
        print('{', i.start, ',', i.end, '}')
