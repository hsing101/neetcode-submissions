class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        cycle = set()
        isStart = -1

        def dfs(node, parent):
            nonlocal isStart
            if node in visited:
                isStart = node
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if isStart != -1:
                        cycle.add(node)
                    if isStart == node:
                        isStart = -1
                    return True
            return False
                    

        
        res = dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []






        