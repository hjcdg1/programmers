import queue


def is_connected(str1, str2):
	N = len(str1)
	diff = 0
	for i in range(N):
		if str1[i] != str2[i]:
			diff += 1
		if diff == 2:
			return False
	return True


def solution(begin, target, words):
	if target not in words:
		return 0

	N = len(words) + 1
	nvs = [[] for _ in range(N)]

	for i, word in enumerate(words):
		if is_connected(begin, word):
			nvs[0].append(i + 1)

	for i in range(N - 1):
		for j in range(N - 1):
			if is_connected(words[i], words[j]) and i != j:
				nvs[i + 1].append(j + 1)

	target_v = words.index(target) + 1
	q = queue.Queue()
	distance = [-1 for _ in range(N)]

	q.put(0)
	distance[0] = 0

	while q.qsize() > 0:
		v = q.get()
		for nv in nvs[v]:
			if distance[nv] == -1:
				q.put(nv)
				distance[nv] = distance[v] + 1

	if distance[target_v] == -1:
		return 0;
	else:
		return distance[target_v]