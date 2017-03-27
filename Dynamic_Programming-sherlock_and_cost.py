# https://www.hackerrank.com/challenges/sherlock-and-cost/forum
'''
define three functions:
L(i) = max cost using first i items of array B, ending with 1 at i th position. {note: 1 is low so we use L to denote low}
H(i) = max cost for first i items of array B, ending in Bi at i th position. {note: Bi is higher of 1 or Bi thus use H to denote that}
F(i) = max cost for first i items regardless of ending.
L(i) = max (L(i-1)+|1-1|,H(i-1)+|B(i-1) - 1|)
H(i) = max (H(i-1)+|B(i)-B(i-1)|,L(i-1)+|B(i) - 1|)
F(i) = max(L(i),H(i))


'''



for _ in range(int(input())):
	n = int(input())
	# b = (str(raw_input()).split())
	b = raw_input()
	b = [int(x) for x in b.split()]

	# l1, l2 = 0, 0
	l, h = 0, 0
	for i in range(1, n):
		l, h = (max(l, h + b[i - 1] - 1),
				max(l + b[i] - 1, h))
		# if i % 2 != 0: 
		# 	l += b[i] - 1
		# 	h += b[i-1] - 1
		# else:
		# 	l += b[i-1] - 1
		# 	h += b[i] - 1


	print(max(l, h))



