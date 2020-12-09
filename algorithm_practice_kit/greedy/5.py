def get_parent(parent, v):
	if parent[v] == -1:
		return v
	else:
		result = get_parent(parent, parent[v])
		parent[v] = result
		return result


def is_same_set(parent, v1, v2):
	p1, p2 = get_parent(parent, v1), get_parent(parent, v2)
	return True if p1 == p2 else False


def union(parent, v1, v2):
	p1, p2 = get_parent(parent, v1), get_parent(parent, v2)
	parent[p2] = p1


def solution(n, costs):
	edges = sorted(costs, key=lambda x: x[2])
	parent = [-1 for _ in range(n)]

	answer = 0
	for edge in edges:
		v1, v2, cost = tuple(edge)
		if not is_same_set(parent, v1, v2):
			union(parent, v1, v2)
			answer += cost

	return answer