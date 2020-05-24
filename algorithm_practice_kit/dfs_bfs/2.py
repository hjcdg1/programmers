def dfs(v, nvs, visited, component):
	visited[v] = True
	component.append(v)

	for nv in nvs[v]:
		if not visited[nv]:
			dfs(nv, nvs, visited, component)



def solution(n, computers):
	nvs = [[] for _ in range(n)]
	for v1 in range(n):
		for v2 in range(n):
			if computers[v1][v2] == 1 and v1 != v2:
				nvs[v1].append(v2)

	components = []
	visited = [False for _ in range(n)]
	for v in range(n):
		if not visited[v]:
			component = []
			dfs(v, nvs, visited, component)
			components.append(component)

	return len(components)