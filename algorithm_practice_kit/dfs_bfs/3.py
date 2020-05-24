def is_connected(str1, str2):
	N = len(str1)
	diff = 0
	for i in range(N):
		if str1[i] != str2[i]:
			diff += 1
		if diff == 2:
			return False
	return True

def dfs(v, nvs, visited, target_v):
	if v == target_v:
		return 0

	visited[v] = True
	min_cnt = float('inf')
	for nv in nvs[v]:
		if not visited[nv]:
			min_cnt = min(min_cnt, 1 + dfs(nv, nvs, visited, target_v))

	visited[v] = False
	return min_cnt

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
	visited = [False for _ in range(N)]
	answer = dfs(0, nvs, visited, target_v)

	return answer if answer != float('inf') else 0