class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        profit=0
        while j<len(prices):
            m_profit=0
            if prices[j]>prices[i]:
                m_profit=prices[j]-prices[i]
                profit=max(profit,m_profit)
                j+=1
            else:
                i=j
                j+=1
        return profit


        
