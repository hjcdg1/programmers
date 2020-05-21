def solution(participant, completion):
    hash_table = {}
    for p in participant:
    	if p not in hash_table:
    		hash_table[p] = 0
    	hash_table[p] += 1

    for c in completion:
    	hash_table[c] -= 1

    for key, value in hash_table.items():
    	if value != 0:
    		return key