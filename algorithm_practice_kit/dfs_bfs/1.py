def dfs(numbers, idx, target):
	if idx == len(numbers) - 1:
		if numbers[idx] == target or -numbers[idx] == target:
			return 1
		else:
			return 0
	return dfs(numbers, idx + 1, target - numbers[idx]) + dfs(numbers, idx + 1, target + numbers[idx])


def solution(numbers, target):
	return dfs(numbers, 0, target)