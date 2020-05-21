def solution(clothes):
	hash_table = {}
	for c in clothes:
		if c[1] not in hash_table:
			hash_table[c[1]] = 0
		hash_table[c[1]] += 1

	answer = 1
	for key, value in hash_table.items():
		answer *= value + 1
	return answer - 1