def solution(priorities, location):
	N = len(priorities)
	priorities = [{'id': i, 'p': p} for i, p in enumerate(priorities)]

	new_N = N
	answer = []
	idx = 0

	while True:
		p = priorities[idx]['p']
		
		is_found = False
		for j in range(idx + 1, new_N):
			if priorities[j]['p'] > p:
				is_found = True
				break
		if is_found:
			priorities.append(priorities[idx])
			new_N += 1
		else:
			answer.append(priorities[idx])
			if len(answer) == N:
				break

		idx += 1

	for idx, data in enumerate(answer):
		if data['id'] == location:
			return idx + 1