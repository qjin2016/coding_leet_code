'''
reference: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

O(n^2)

some potential applications:
1, output k largest/smallest values O(k*n)
2, check if an array is sorted O(n)

'''

def bubbleSort(alist):
	for i in range(len(alist)-1, 0, -1):
		for j in range(i):
			if alist[j+1] < alist[j]:
				# swap
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp
	return alist

if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	sorted_list = bubbleSort(alist)
	print(sorted_list)