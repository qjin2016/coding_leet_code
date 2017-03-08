'''
346,

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
'''

from collections import deque

class MovingAverage(object):

	def __init__(self, size):
		self.__size = size
		self.__sum = 0
		self.__q = deque([])

	def next(self, val):
		if len(self.__q) == self.__size:
			self.__sum -= self.__q.popleft()
		self.__q.append(val)
		self.__sum += val
		return 1.0 * self.__sum / len(self.__q)

if __name__ == '__main__':
	obj = MovingAverage(3)
	print(obj.next(1))
	print(obj.next(2))
	print(obj.next(3))
	print(obj.next(4))