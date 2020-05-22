import queue

def solution(n, edge):
	distance = [-1 for _ in range(n + 1)]
	neighbors = [[] for _ in range(n + 1)]
	for e in edge:
		neighbors[e[0]].append(e[1])
		neighbors[e[1]].append(e[0])

	q = queue.Queue()

	q.put(1)
	distance[1] = 0

	while q.qsize() > 0:
		v = q.get()
		for neighbor in neighbors[v]:
			if distance[neighbor] == -1:
				q.put(neighbor)
				distance[neighbor] = distance[v] + 1

	max_d = max(distance[1:])

	cnt = 0
	for d in distance[1:]:
		if d == max_d:
			cnt += 1

	return cnt