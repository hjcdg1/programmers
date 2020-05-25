def binary_search(budgets, M, start, end):
	if start == end:
		return start

	mid = (start + end + 1) // 2
	total_budget = sum([min(budget, mid) for budget in budgets])
	if total_budget == M:
		return mid
	elif total_budget < M:
		return binary_search(budgets, M, mid, end)
	else:
		return binary_search(budgets, M, start, mid - 1)

def solution(budgets, M):
	N = len(budgets)
	max_budget = max(budgets)
	return binary_search(budgets, M, 0, max_budget)

print(solution([120, 110, 140, 150], 485))