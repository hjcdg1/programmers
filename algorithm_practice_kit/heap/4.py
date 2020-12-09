import heapq


def solution(stock, dates, supplies, k):
	N = len(dates)

	zero_day = stock
	cnt = 0
	i = 0
	h = []

	while True:
		if zero_day >= k:
			break
		else:
			while True:
				if i < N and dates[i] <= zero_day:
					heapq.heappush(h, -supplies[i])
					print("힙에 {} 추가".format(supplies[i]))
					i += 1
				else:
					break
			zero_day += -heapq.heappop(h)
			cnt += 1
			print("구간 {}로 확장".format(zero_day))

	return cnt