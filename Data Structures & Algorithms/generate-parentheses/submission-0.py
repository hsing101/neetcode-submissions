class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = defaultdict(int)
        temp = []
        soln = []
        def dfs():
            if len(temp) == 2 * n :
                soln.append("".join(temp.copy()))
                return
            if len(temp) > 2 * n:
                return
            if brackets['('] < n:
                temp.append('(')
                brackets['('] += 1
                dfs()
                temp.pop()
                brackets['('] -= 1
            if brackets[')'] < brackets['(']:
                temp.append(')')
                brackets[')'] += 1
                dfs()
                temp.pop()
                brackets[')'] -= 1

        dfs()
        return soln
                
            

