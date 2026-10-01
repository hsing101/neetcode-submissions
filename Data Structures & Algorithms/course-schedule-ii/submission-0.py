class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        output = []
        visited = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in adj[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output
                




        
        
        
        

        