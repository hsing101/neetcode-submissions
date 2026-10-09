class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, 0
        l_max, r_max = [], []
        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
            l_max.append(l)
        for i in range(len(height) -1, -1, -1):
            if height[i] > r:
                r = height[i]
            r_max.append(r)
        r_max.reverse()
        i = 0
        for (l, r) in zip(l_max, r_max):
            min_height = min(l , r)
            water += (min_height - height[i])
            i += 1
        return water


        