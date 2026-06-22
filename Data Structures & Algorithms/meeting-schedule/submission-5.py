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
            if visited[i][0] < visited[i - 1][1]:
                return False
        return True                  