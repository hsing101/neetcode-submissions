"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        visited = []
        for interval in intervals:
            i, j = interval.start, interval.end
            visited.append((i, j))
        visited.sort()
        for i in range (1, len(visited)):
            ps, s = visited[i - 1][0], visited[i][0]
            pe, e = visited[i - 1][1], visited[i][1]
            if s < pe:
                return False
        return True                  