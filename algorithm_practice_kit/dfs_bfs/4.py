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

"""
<another solution>

def dfs(idx, nvs, total_tickets_cnt, tickets_cnt, path):
	# 현재 도시 방문
	path.append(idx)

	# 모든 항공권 사용 완료
	if len(path) == total_tickets_cnt + 1:
		return True

	# 올바른 경로가 존재하는지 여부
	path_exists = False

	# 이웃 도시들에 대해 루프
	for nv in nvs[idx]:
		# 해당 도시를 가기 위한 항공권이 없는 경우
		if tickets_cnt[idx][nv] == 0:
			continue

		# 항공권 사용
		tickets_cnt[idx][nv] -= 1
		path_exists = True

		# 해당 도시 방문 시도 (DFS 재귀 호출)
		result = dfs(nv, nvs, total_tickets_cnt, tickets_cnt, path)

		# 잘못된 경로였다면, 사용한 항공권 회수
		if not result:
			tickets_cnt[idx][nv] += 1
			path_exists = False

	if not path_exists:
		path.pop()
		return False
	else:
		return True


def solution(tickets):
	# 도시(정점) 정보
	V_set = set()
	for ticket in tickets:
		V_set.add(ticket[0])
		V_set.add(ticket[1])
	V_len = len(V_set)
	V_list = list(V_set)  # convert int -> str
	V_map = dict([(name, idx) for idx, name in enumerate(V_list)])  # convert str -> int

	# 항공권(간선) 정보
	nvs = [[] for _ in range(V_len)]
	total_tickets_cnt = len(tickets)
	tickets_cnt = [[0 for _ in range(V_len)] for _ in range(V_len)]
	for ticket in tickets:
		ticket_from, ticket_to = V_map[ticket[0]], V_map[ticket[1]]
		nvs[ticket_from].append(ticket_to)
		tickets_cnt[ticket_from][ticket_to] += 1

	# 도시 이름을 기준으로 항공권 정렬
	for nv_list in nvs:
		nv_list.sort(key=lambda v: V_list[v])

	path = []
	dfs(V_map['ICN'], nvs, total_tickets_cnt, tickets_cnt, path)

	return list(map(lambda v: V_list[v], path))
"""