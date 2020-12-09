from itertools import permutations


def get_strike_ball(a, b):
	a, b = str(a), str(b)

	ball_cnt = len(set(a) & set(b))
	strike_cnt = 0
	for i in range(len(a)):
		if a[i] == b[i]:
			strike_cnt += 1
			ball_cnt -= 1
	return strike_cnt, ball_cnt


def solution(baseball):
	candidates = [int(''.join(p)) for p in permutations('123456789', 3)]

	for b in baseball:
		number, strike, ball = tuple(b)
		new_candidates = []
		for candidate in candidates:
			if (strike, ball) == get_strike_ball(number, candidate):
				new_candidates.append(candidate)
		candidates = new_candidates

	return len(candidates)