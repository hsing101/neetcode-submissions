class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""
        memo = {}
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if (i, j) in memo:
                    if memo[(i, j)]:
                        if len(substring) >= len(curr):
                            curr = substring
                    continue

                if len(substring) < len(curr):
                    continue

                l, r = 0, len(substring) - 1
                flag = True
                
                while l <= r:
                    if substring[l] == substring[r]:
                        l += 1
                        r -= 1
                    else:
                        flag = False
                        break
                memo[(i, j)] = flag

                if flag:
                    curr = substring
        return curr
        







        