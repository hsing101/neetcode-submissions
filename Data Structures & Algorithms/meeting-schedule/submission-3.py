"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        visited = set()
        for interval in intervals:
            i, j = interval.start, interval.end
            for n, m in visited:
                if i >= m or j <= n:
                    continue
                else:
                    return False 
            visited.add((i, j))
        return True
            