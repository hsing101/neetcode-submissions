class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p2] = p1
                size[p1] += size[p2]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return[n1, n2]







        