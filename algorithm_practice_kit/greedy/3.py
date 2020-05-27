def solution(number, k):
	number = list(map(int, list(number)))
	N = len(number)

	stack = []
	remove_cnt = 0
	for n in number:
		while remove_cnt < k and stack and stack[-1] < n:
			stack.pop()
			remove_cnt += 1
		stack.append(n)
	return str(int(''.join(map(str, stack[:N - k]))))