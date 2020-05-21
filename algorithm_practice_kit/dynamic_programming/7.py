def solution(K, travel):
	N = len(travel)

	D = [[0 for _ in range(K + 1)] for _ in range(N)]

	for j in range(1, K + 1):
		if travel[N - 1][0] <= j:
			D[N - 1][j] = max(D[N - 1][j], travel[N - 1][1])
		if travel[N - 1][2] <= j:
			D[N - 1][j] = max(D[N - 1][j], travel[N - 1][3])

	for i in reversed(range(N - 1)):
		for j in range(1, K + 1):
			if travel[i][0] <= j:
				D[i][j] = max(D[i][j], travel[i][1] + D[i + 1][j - travel[i][0]])
			if travel[i][2] <= j:
				D[i][j] = max(D[i][j], travel[i][3] + D[i + 1][j - travel[i][2]])

	return D[0][K]