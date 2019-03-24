# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        i = 0
        while i < len(intervals) and intervals[i].start < new_interval.start:
            i += 1

        intervals.insert(i, new_interval)

        # return intervals
        return self.merge(intervals)

    def merge(self, intervals):
        ans = list()
        start, end = intervals[0].start, intervals[0].end

        for i in range(len(intervals)):
            end = max(end, intervals[i].end)

            if i == len(intervals) - 1 or intervals[i + 1].start > end:
                ans.append(Interval(start, end))
                if i < len(intervals) - 1:
                    start = intervals[i + 1].start
        return ans


if __name__ == "__main__":
    s = Solution()
    interval = s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)],
                        Interval(4, 9))

    for i in interval:
        print('{', i.start, ',', i.end, '}')