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

	if answer[0] == '0':
		return '0'
	else:
		return answer