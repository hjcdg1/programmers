def solution(arrangement):
	stack = []
	piece_cnt = 0
	open_bracket_cnt = 0

	for c in arrangement:
		if c == '(':
			if stack and stack[-1]['val'] == '(':
				stack[-1]['is_bar'] = True
			stack.append({'val': '(', 'is_bar': False})
			open_bracket_cnt += 1
		else:
			top = stack.pop()
			open_bracket_cnt -= 1
			if top['is_bar']:
				piece_cnt += 1
			else:
				piece_cnt += open_bracket_cnt

	return piece_cnt