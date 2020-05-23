def solution(prices):
	N = len(prices)

	answer = []
	for i in range(N):
		price = prices[i]
		cnt = 0
		for j in range(i + 1, N):
			cnt += 1
			if prices[j] < price:
				break
		answer.append(cnt)
	return answer