class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
        	return 0
        profit = 0
        minPrice = prices[0]
        for x in range(1,len(prices)):
        	minPrice = min(minPrice,prices[x])
        	profit = max(profit,prices[x]-minPrice)
        return profit




if __name__ == '__main__':
	p = Solution()
	prices = [[4,5,6,1,3,4,8],[4,56,5],[2],[3,4]]
	for x in prices:
		print(p.maxProfit(x))