class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        alist = defaultdict(list)
        parents = defaultdict(int)

        for a, b in edges:
            if a == b:
                return False
            alist[a].append(b)
            alist[b].append(a)
            parents[b] = a
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
                    elif j != parents[node]:
                        return False
                    
            return len(visited) == n
        
        return bfs(0)
