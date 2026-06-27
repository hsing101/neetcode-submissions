class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        def dfs(i, prev):
            if i == len(intervals):
                return 0
             # Option 1: remove current interval
            remove = dfs(i + 1, prev)

            # Option 2: keep current interval if no overlap
            if prev == -1 or intervals[i][0] >= intervals[prev][1]:
                remove = max(remove, 1 + dfs(i + 1, i))

            return remove

        return len(intervals) - dfs(0, -1)

            
                