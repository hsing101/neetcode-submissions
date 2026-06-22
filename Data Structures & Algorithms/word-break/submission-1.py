class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxlen = 0
        wordset = set(wordDict)
        memo = {}
        for word in wordDict:
            maxlen = max(maxlen, len(word))

        def dfs(s):
            if len(s) == 0:
                return True
            if s in memo:
                return memo[s]
            for i in range(1, maxlen + 1):
                if s[ : i] in wordset:
                    if dfs(s[i: ]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False

        return dfs(s)
        