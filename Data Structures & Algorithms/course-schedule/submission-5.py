class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        alist = defaultdict(list)

        for a, b in prerequisites:
            alist[a].append(b)

        visited = set()

        def dfs(num):
            if alist[num] == []:
                return True
            if num in visited:
                return False
            visited.add(num)
            for nei in alist[num]:
                if not dfs(nei):
                    return False
            visited.remove(num)
            alist[num] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
             
            