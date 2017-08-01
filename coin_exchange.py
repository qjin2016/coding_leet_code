def DPcc(coinlist, change):
	coinCounts = list(range(change + 1))
	for coin in coinCounts:
		coinCount= coin
		for j in [c for c in coinlist if c < coinCount]:
			if (coinCounts[coin - j] + 1) < coinCount:
				coinCounts[coin] = coinCounts[coin - j] + 1
	return coinCounts
if __name__ == '__main__':
	print(DPcc([1, 5, 10, 25], 63))