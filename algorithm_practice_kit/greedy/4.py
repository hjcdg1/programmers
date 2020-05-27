def solution(people, limit):
	N = len(people)
	people.sort(reverse=True)

	boat_cnt = 0
	stack = []
	for curr in people:
		if stack and stack[-1] >= curr:
			stack.pop()
		else:
			boat_cnt += 1
			stack.append(limit - curr)

	return boat_cnt