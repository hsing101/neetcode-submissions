class Solution:
    def isPalindrome(self, s: str) -> bool:
        listt = []
        for char in s:
            if char.isalnum():
                listt.append(char.lower())
        i,j = 0,len(listt)-1
        while i < j:
            if listt[i]!=listt[j]:
                return False
            i += 1
            j -= 1
        return True
        

        