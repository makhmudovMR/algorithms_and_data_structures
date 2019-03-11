'''
	left(index) index * 2
	right(index) index * 2 + 1
	parent(index) index // 2
'''

# class MaxHeap
# public functions: peek(), pop(), push()
# private functions: __swap(), __floatUp(), __bubbleDown()

class MaxHeap:

	def __init__(self, items=[]):
		self.heap = [0]
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap) - 1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False

	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap)-1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max

	def push(self, item):
		self.heap.append(item)
		self.__floatUp(len(self.heap) - 1)

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index // 2
		if index <= 1:
			return 
		elif self.heap[parent] < self.heap[index]:
			self.__swap(index, parent)
			self.__floatUp(index // 2)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index

		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)
		
def main():
	heap = MaxHeap([100, 50, 20, 10, 5])
	for _ in range(5):
		print(heap.pop())

main()