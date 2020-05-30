def dfs(v, nvs, order, used_cnt, available_cnt, E_len):
	# 노드 v 방문
	order.append(v)
	
	# 모든 간선 사용 완료 (성공적으로 끝)
	if used_cnt[0] == E_len:
		return True  # Success

	# 아직 사용할 간선 남음
	else:
		# 이웃 정점 방문 (사용되지 않은 간선에 대해서만)
		visit = False
		for nv in nvs[v]:
			if available_cnt[v][nv] > 0:
				available_cnt[v][nv] -= 1
				used_cnt[0] += 1
				visit = True
				if not dfs(nv, nvs, order, used_cnt, available_cnt, E_len):
					available_cnt[v][nv] += 1
					used_cnt[0] -= 1
					visit = False

		# 방문한 이웃이 없음 (사용되어야 하는 간선은 남았는데 길이 막힘)
		if not visit:
			order.pop()
			return False  # Fail
		else:
			return True  # Success

def solution(tickets):
	# 노드 종류
	V = set()
	for ticket in tickets:
		V.add(ticket[0])
		V.add(ticket[1])
	V_len = len(V)
	E_len = len(tickets)

	# 노드 번호 -> 이름
	int_to_str = list(sorted(list(V)))

	# 노드 이름 -> 번호
	str_to_int = dict([(v, idx) for idx, v in enumerate(int_to_str)])

	# 각 노드의 이웃 정점 찾기
	nvs = [[] for _ in range(V_len)]
	available_cnt = [[0 for _ in range(V_len)] for _ in range(V_len)]
	for ticket in tickets:
		start = str_to_int[ticket[0]]
		end = str_to_int[ticket[1]]
		nvs[start].append(end)
		available_cnt[start][end] += 1

	# 이웃 정점 정렬
	for nv in nvs:
		nv.sort()

	# DFS 수행
	order = []
	dfs(str_to_int['ICN'], nvs, order, [0], available_cnt, E_len)
	return [int_to_str[o] for o in order]