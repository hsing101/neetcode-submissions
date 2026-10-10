class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = defaultdict(list)

        for src, dst in reversed(sorted(tickets)):
            graph[src].append(dst)

        def dfs(airport) :
            while airport in graph and graph[airport]:
                dfs(graph[airport].pop())
            res.append(airport)

        dfs('JFK')
        return res[::-1]

