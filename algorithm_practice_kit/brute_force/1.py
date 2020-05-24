def solution(answers):
	p0 = [1, 2, 3, 4, 5]
	p1 = [2, 1, 2, 3, 2, 4, 2, 5]
	p2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

	cnt = [0, 0, 0]
	for i, answer in enumerate(answers):
		if answer == p0[i % 5]:
			cnt[0] += 1
		if answer == p1[i % 8]:
			cnt[1] += 1
		if answer == p2[i % 10]:
			cnt[2] += 1

	answer = []
	max_cnt = max(cnt)
	for i, c in enumerate(cnt):
		if c == max_cnt:
			answer.append(i + 1)
	return answer