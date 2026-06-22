class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        soln = []
        curr = []
        def dfs(i, curr, k):
            if len(curr) == k:
                soln.append(curr[:])
                return
            if i > n:
                return
            curr.append(i)
            dfs(i + 1, curr, k)
            curr.pop()
            dfs(i + 1, curr, k)
        dfs(1, curr, k)
        return soln