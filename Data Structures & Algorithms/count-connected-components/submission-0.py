class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        alist = defaultdict(list)
        for a, b in edges:
            alist[a].append(b)
            alist[b].append(a)
        
        visited = set()


        def bfs(num):
            queue = deque()
            visited.add(num)
            queue.append(num)
            while queue:
                node = queue.pop()
                for j in alist[node]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
        
        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        
        return count


