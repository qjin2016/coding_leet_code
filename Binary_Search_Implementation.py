'''
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
'''

def binarySearch(alist, item):
	'''
	alist is a sorted list
	'''
	if len(alist) == 0:
		return False
	midpoint = len(alist) // 2
	if alist[midpoint] == item:
		return True
	else:
		if item < alist[midpoint]:
			return binarySearch(alist[:midpoint], item)
		else:
			return binarySearch(alist[midpoint + 1:], item)

def binarySearch2(alist, item):
	if len(alist) == 0:
		return False
	found = False
	midpoint = len(alist) // 2
	minpoint = 0
	maxpoint = len(alist)
	while minpoint < maxpoint:
		if alist[midpoint] == item:
			return True
		elif item < alist[midpoint]:
			maxpoint = midpoint
			midpoint = (minpoint + maxpoint) // 2
		else:
			minpoint = midpoint + 1
			midpoint = (minpoint + maxpoint) // 2
	return found


if __name__ == '__main__':
	print (binarySearch2([0, 1, 2, 8, 13, 17, 19, 32, 42], 3))
	print (binarySearch2([0, 1, 2, 8, 13, 17, 19, 32, 42], 0))