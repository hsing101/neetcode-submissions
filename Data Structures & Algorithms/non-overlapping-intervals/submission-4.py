class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        def dfs(i, prev_end):
            if i == len(intervals):
                return 0
             # Option 1: remove current interval
            remove = 1 + dfs(i + 1, prev_end)

            # Option 2: keep current interval if no overlap
            keep = float('inf')
            if intervals[i][0] >= prev_end:
                keep = dfs(i + 1, intervals[i][1])

            return min(remove, keep)

        return dfs(0, float('-inf'))

            
                