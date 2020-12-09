def solution(number, k):
	numbers = list(map(int, list(number)))
	N = len(numbers)

	stack = []
	remove_cnt = 0
	for n in numbers:
		while remove_cnt < k and stack and stack[-1] < n:
			stack.pop()
			remove_cnt += 1
		stack.append(n)
	return ''.join(map(str, stack[:N - k]))