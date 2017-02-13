'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

which is equilent to:
find i and j, which maximize Aj - Ai, while i < j
'''

class Solution(object):
	# a naive approach
	def maxProfit(self, prices):
		max_profit = 0
		for i in range(len(prices)):
			for j in range(i+1, len(prices)):
				diff = prices[j] - prices[i]
				if diff > max_profit:
					max_profit = diff
		return max_profit

	def maxProfit2(self, prices):
		max_profit, min_price = 0, float('inf')
		for price in prices:
			min_price = min(price, min_price)
			max_profit = max(max_profit, price-min_price)
		return max_profit


if __name__ == '__main__':
	print 'Solution 1: '
	print Solution().maxProfit([7, 1, 5, 3, 6, 4])
	print 'Solution 2: '
	print Solution().maxProfit2([7, 1, 5, 3, 6, 4])


