class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapp = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(num):
            if len(num) <= 0:
                return []
            strings = backtrack(num[1:])
            listt = []
            if strings == []:
                return list(mapp[num[0]])
            for char in mapp[num[0]]:
                for string in strings:
                    listt.append(char + string)
            return listt
        
        return backtrack(digits)




        