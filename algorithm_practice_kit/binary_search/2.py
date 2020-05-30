def binary_search(n, times, i, j):
	if i == j:
		return i

	mid = (i + j) // 2
	
	# 주어진 시간에 처리할 수 있는 최대 사람 수
	possible_number = 0
	for time in times:
		possible_number += mid // time
	
	# 불가능
	if n > possible_number:
		return binary_search(n, times, mid + 1, j)
	else:
		return binary_search(n, times, i, mid)

def solution(n, times):
	max_time = max(times) * n
	return binary_search(n, times, 1, max_time)