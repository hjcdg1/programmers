def solution(routes):
	routes.sort(key=lambda x: x[1], reverse=True)

	camera_cnt = 1
	range_start, range_end = tuple(routes[0])

	for route in routes[1:]:
		start, end = tuple(route)
		
		# 구간 겹침
		if end >= range_start:
			range_start = max(range_start, start)
			range_end = end
		
		# 구간 안 겹침
		else:
			camera_cnt += 1
			range_start = start
			range_end = end

	return camera_cnt