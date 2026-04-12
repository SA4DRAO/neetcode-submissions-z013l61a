class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0        
        
        maxOnRight = [0]
        pricesCopy = prices
        pricesCopy.reverse()

        for i in range(1, len(pricesCopy)):
            maxOnRight.append(max(maxOnRight[i-1], pricesCopy[i-1]))
        maxOnRight.reverse()
        print(maxOnRight)
        
        maxProfit = 0
        prices.reverse()
        print(maxOnRight)
        for i in range(0,len(prices)-1):
            maxProfit = max(maxProfit, maxOnRight[i] - prices[i])
        return maxProfit