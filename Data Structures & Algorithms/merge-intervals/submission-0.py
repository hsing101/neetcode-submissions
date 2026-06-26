class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]
        for l, r in intervals:
            if l <= output[-1][1]:
                output[-1][1] = max(r, output[-1][1])
            else:
                output.append([l, r])
        return output
