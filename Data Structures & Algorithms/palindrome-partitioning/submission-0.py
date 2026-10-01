class Solution:
    def partition(self, s: str) -> List[List[str]]:
        soln = []
        temp = []
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i):
            if i >= len(s):
                soln.append(temp.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    temp.append(s[i : j + 1])
                    dfs(j + 1)
                    temp.pop()
        dfs(0)
        return soln

        