def solution(n, results):
	D = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

	for result in results:
		D[result[0]][result[1]] = 1

	for k in range(1, n + 1):
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				D[i][j] = min(D[i][j], D[i][k] + D[k][j])

	cnt = 0
	for i in range(1, n + 1):
		is_undefined = False
		for j in range(1, n + 1):
			if i == j:
				continue
			if D[i][j] == float('inf') and D[j][i] == float('inf'):
				is_undefined = True
				break
		if not is_undefined:
			cnt += 1

	return cnt