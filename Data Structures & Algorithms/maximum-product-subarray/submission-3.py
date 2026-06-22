class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        segments = []
        temp = []
        for num in nums:
            if num == 0:
                if temp:
                    segments.append(temp)
                    temp = []
                continue
            temp.append(num)

        if temp:
            segments.append(temp)

        ans = max(nums)
        for segment in segments:
            negs = 0
            for num in segment:
                if num < 0:
                    negs += 1
        
            if negs % 2 == 1:
                first = 0
                last = len(segment) - 1
                for i in range(len(segment)):
                    if segment[i] < 0:
                        first = i
                        break
                for i in range(len(segment) - 1, -1, -1):
                    if segment[i] < 0:
                        last = i
                        break
                if first + 1 < len(segment):
                    prod1 = 1
                    for i in range(first + 1, len(segment)):
                        prod1 *= segment[i]
                    ans = max(ans, prod1)
                
                if last > 0:
                    prod2 = 1
                    for i in range(last):
                        prod2 *= segment[i]
                    ans = max(ans, prod2)
            else:
                prod = 1
                for i in range(len(segment)):
                    prod *= segment[i]
                ans = max(ans, prod)
        return ans