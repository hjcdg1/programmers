from functools import cmp_to_key

def compare(a, b):
	c1, c2 = int(a + b), int(b + a)
	if c1 > c2:
		return -1
	elif c1 < c2:
		return 1
	else:
		return 0

def solution(numbers):
	numbers = list(map(str, numbers))
	numbers.sort(key=cmp_to_key(compare))
	answer = ''.join(numbers)

	start = -1
	for i, c in enumerate(answer):
		if c != '0':
			start = i
			break
	if start == -1:
		return '0'
	else:
		return answer[start:]