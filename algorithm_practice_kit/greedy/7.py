def solution(weight):
	weight.sort()
	max_w = weight[0]

	for w in weight[1:]:
		if w <= max_w + 1:
			max_w += w
		else:
			break
	return max_w + 1