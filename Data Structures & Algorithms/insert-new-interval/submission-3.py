class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1 

        low = newInterval[0]
        high = newInterval[1]
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            low = min(low, intervals[i][0])
            high = max(high, intervals[i][1])
            i += 1
        res.append([low, high])
        res.extend(intervals[i:])
        return res