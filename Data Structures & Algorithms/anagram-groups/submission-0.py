class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln={}
        words = set()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in words:
                soln[sorted_word].append(word)
            else:
                soln[sorted_word] = [word]
                words.add(sorted_word)
        return list(soln.values())



            

        

        