if __name__ == '__main__':
	n = int(10)
	# b = (str(raw_input()).split())
	b = '55 68 31 80 57 18 34 28 76 55'
	b = [int(x) for x in b.split()]
	if n == 1:
		print(0)
	else:
		l, h = 0, 0
		for i in range(1, n):
			l, h = h + b[i - 1] - 1, l + b[i] - 1
		print(max(l, h))
