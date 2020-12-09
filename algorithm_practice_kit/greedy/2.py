def get_min_diff(current, target):
	current_int = ord(current)
	target_int = ord(target)
	if current_int > target_int:
		return min(current_int - target_int, ord('Z') - current_int + 1 + target_int - ord('A'))
	elif current_int < target_int:
		return min(target_int - current_int, ord('Z') - target_int + 1 + current_int - ord('A'))
	else:
		return 0


def get_left(N, current_arr, target_arr, i):
	move_cnt = 0
	while current_arr[i] == target_arr[i]:
		if i > 0:
			i -= 1
		else:
			i = N - 1
		move_cnt += 1
		if move_cnt == N:
			return -1
	return move_cnt


def get_right(N, current_arr, target_arr, i):
	move_cnt = 0
	while current_arr[i] == target_arr[i]:
		if i < N - 1:
			i += 1
		else:
			i = 0
		move_cnt += 1
		if move_cnt == N:
			return -1
	return move_cnt


def get_prev_n(N, i, left):
	if i - left >= 0:
		return i - left
	else:
		return N + i - left


def get_next_n(N, i, right):
	if i + right < N:
		return i + right
	else:
		return i + right - N


def solution(name):
	N = len(name)
	current_arr = ['A' for _ in range(N)]
	target_arr = list(name)

	i = 0
	cnt = 0
	while True:
		# 현재 알파벳 수정
		cnt += get_min_diff(current_arr[i], target_arr[i])
		current_arr[i] = target_arr[i]

		# 불일치한 알파벳 찾을 때까지 이동하는 횟수
		left = get_left(N, current_arr, target_arr, i)
		right = get_right(N, current_arr, target_arr, i)
		
		# 불일치 알파벳 X
		if left == -1 or right == -1:
			break

		# 왼쪽으로 이동하는 것이 이득
		elif left < right:
			cnt += left
			i = get_prev_n(N, i, left)

		# 오른쪽으로 이동하는 것이 이득
		else:
			cnt += right
			i = get_next_n(N, i, right)

	return cnt