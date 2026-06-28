class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)
        while l <= r:
            time = 0
            m = (l + r) // 2
            for pile in piles:
                time += math.ceil(pile/m)
            if time <= h:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
                
        return ans