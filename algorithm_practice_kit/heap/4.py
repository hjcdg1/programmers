import heapq

def solution(operations):
	max_h = []
	min_h = []

	size = 0
	for operation in operations:
		op, data = tuple(operation.split())
		data = int(data)

		if op == 'I':
			heapq.heappush(max_h, -data)
			heapq.heappush(min_h, data)
			size += 1
		else:
			if size > 0:
				if data == 1:
					heapq.heappop(max_h)
				else:
					heapq.heappop(min_h)
				size -= 1

			if size == 0:
				max_h = []
				min_h = []

	if size == 0:
		return [0, 0]
	else:
		return [-heapq.heappop(max_h), heapq.heappop(min_h)]