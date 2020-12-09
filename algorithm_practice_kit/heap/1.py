import heapq


def solution(scoville, K):
	heapq.heapify(scoville)

	cnt = 0
	while True:
		s1 = heapq.heappop(scoville)
		if s1 >= K:
			break
		elif not scoville:
			cnt = -1
			break
		else:
			s2 = heapq.heappop(scoville)
			heapq.heappush(scoville, s1 + 2 * s2)
			cnt += 1
	return cnt