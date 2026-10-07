class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i
        i, j, max_idx = 0, 0, 0
        for k in range(i, j + 1):
            max_idx = max(last[s[k]], max_idx) 
        while j < len(s):
            for k in range(i, j + 1):
                max_idx = max(last[s[k]], max_idx) 
            while max_idx > j:
                j = max_idx
                for k in range(i, j + 1):
                    max_idx = max(last[s[k]], max_idx)  
            output.append(j - i + 1)
            j += 1
            i = j
        return output
        
                



        