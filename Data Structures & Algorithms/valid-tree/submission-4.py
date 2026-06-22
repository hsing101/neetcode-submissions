class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        alist = defaultdict(list)

        for a, b in edges:
            if a == b:
                return False
            alist[a].append(b)
            alist[b].append(a)
            
        visited = set()

        def bfs(num, parent):
            queue = deque()
            visited.add(num)
            queue.append((num, parent))
            while queue:
                node, parent = queue.popleft()
                for j in alist[node]:
                    if j not in visited:
                        visited.add(j)
                        queue.append((j, node))
                    elif j != parent:
                        return False
                    
            return len(visited) == n
        
        return bfs(0, -1)
