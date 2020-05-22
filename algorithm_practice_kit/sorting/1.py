def solution(array, commands):
	answer = []
	for command in commands:
		i, j, k = command
		sorted_array = sorted(array[i - 1:j])
		answer.append(sorted_array[k - 1])
	return answer