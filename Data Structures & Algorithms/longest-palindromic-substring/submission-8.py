class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if len(substring) < len(curr):
                    continue
                l, r = 0, len(substring) - 1
                flag = False
                while l <= r:
                    if substring[l] == substring[r]:
                        l += 1
                        r -= 1
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    if len(substring) >= len(curr):
                        curr = substring
        return curr
        







        