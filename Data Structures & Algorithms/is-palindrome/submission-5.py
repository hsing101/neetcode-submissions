class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=len(s)-1
        i=0
        while i<j:
            while s[i].isalnum()==False:
                i+=1
                if i==len(s):
                    return True
            while s[j].isalnum()==False:
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            j-=1
            i+=1
        return True

        