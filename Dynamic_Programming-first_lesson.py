'''
coin exchange problem

http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

'''

# 1, a naive and greedy approach
def recMC(coinValueList, change):
	minCoins = change
	if change in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c < change]:
			numCoins = 1 + recMC(coinValueList, change - i)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins

# 2, avoid re-computing known results, using caching technique
def recMC2(coinValueList, change, known = [0] * 64):
	minCoins = change
	if change in coinValueList:
		return 1
	elif known[change]:
		return known[change]
	else:
		for i in [c for c in coinValueList if c < change]:
			numCoins = 1 + recMC2(coinValueList, change - i, known)
			if numCoins < minCoins:
				minCoins = numCoins
				known[change] = minCoins
	return minCoins

# 3, dynamic programming
def dpMC(coinValueList, change):
	minCoins = [0] * (change + 1)
	for cents in range(change + 1):
		coinCounts = cents
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents - j] + 1 < coinCounts:
				coinCounts = minCoins[cents - j] + 1
		minCoins[cents] = coinCounts
	return minCoins[cents]







if __name__ == '__main__':
	coinValueList = [1, 5, 10, 25]
	change = 63
	# print(recMC(coinValueList, change))
	# print(recMC2(coinValueList, change))
	print(dpMC(coinValueList, change))



