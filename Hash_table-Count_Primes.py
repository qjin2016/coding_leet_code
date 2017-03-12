'''
204,

Count the number of prime numbers less than a non-negative number, n.

'''

class Solution(object):

	# # too slow! time-out!
	# def countPrimes(self, n):
	# 	if n < 3:
	# 		return  0
	# 	count = 0
	# 	for j in range(n-1):
	# 		if j > 0:
	# 			y = j + 1
	# 			if self.PrimeChecker(y):
	# 				count += 1
	# 	return count

	# def PrimeChecker(self, m):
	# 	for i in range(m-1):
	# 		x = i+1
	# 		if (x != 1) and ((m % x) == 0):
	# 			return False
	# 	return True


	# #memory overflow 
	# def countPrimes(self, n):
	# 	if n <= 2:
	# 		return 0

	# 	isPrime = [True] * n
	# 	isPrime[0] = isPrime[1] = False

	# 	for i in range(2, n):
	# 		if isPrime[i]:
	# 			for j in range(i<<1, n, i):
	# 				isPrime[j] = False
	# 	return sum(isPrime)


		def countPrimes(self, n):
			if n <=2:
				return 0

			isPrime = [True] * n
			isPrime[0] = isPrime[1] = False

			for i in range(2, n):
				if isPrime[i]:
					for j in range(i*2, n, i):
						isPrime[j] = False
			isPrime = filter(lambda x:x, isPrime)
			return len(isPrime)




if __name__ == '__main__':
	print(Solution().countPrimes(10))
