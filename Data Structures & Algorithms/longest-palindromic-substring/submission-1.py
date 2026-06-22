class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        sub = 0
        memo = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 in memo:
                    sub = memo[ans]
                    continue
                if memo != {} and j - i + 1 < min(memo.keys()):
                    continue
                l, r = i, j
                while l <= r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l > r and j - i + 1 >= ans:
                    sub = s[i : j + 1]
                    ans = j - i + 1
                    memo[ans] = sub
        return sub






        