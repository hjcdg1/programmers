def solution(citations):
	N = len(citations)
	citations.sort()

	h = 0

	for c in range(1, citations[0]):
		if c - 1 < N:
			h = c

	for idx, c in enumerate(citations):
		if idx + c - 1 < N:
			h = c
			if (idx + 1 < N) and (citations[idx + 1] > c + 1):
				curr = c + 1
				while curr < citations[idx + 1]:
					if idx + curr < N:
						h = curr
					curr += 1

	return h