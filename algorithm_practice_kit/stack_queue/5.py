def solution(heights):
	N = len(heights)

	answer = [0]
	for i, h1 in enumerate(heights[1:], start=1):
		pos = -1
		for j in reversed(range(i)):
			if heights[j] > h1:
				pos = j
				break
		answer.append(pos + 1 if pos != -1 else 0)

	return answer

"""
<more efficient solution>

def solution(heights):
	N = len(heights)
	stack = []
	answer = [-1] + [0 for _ in range(N)]

	for i, h in enumerate(reversed(heights)):
		idx = N - i

		while stack:
			top = stack[-1]
			if top[0] < h:
				stack.pop()
				answer[top[1]] = idx
			else:
				break

		stack.append((h, idx))

	return answer[1:]
"""