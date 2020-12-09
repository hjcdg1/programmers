import queue


def solution(bridge_length, weight, truck_weights):
	N = len(truck_weights)
	truck_weights.reverse()
	on_road = queue.Queue()
	cross_road_cnt = 0
	rw = weight

	sec = 0
	while True:
		# 도착한 트럭이 있다면 도로에서 제거 (버블이 도착했으면 아무 변화 X)
		if on_road.qsize() >= bridge_length:
			arrive_weight = on_road.get()
			if arrive_weight != 0:
				rw += arrive_weight
				cross_road_cnt += 1

		# 모든 트럭이 도착했으면 종료
		if cross_road_cnt == N:
			break

		# 새 트럭을 도로에 올릴 수 있는지 확인 (없으면 버블 삽입)
		if truck_weights and rw >= truck_weights[-1]:
			curr_wegiht = truck_weights.pop()
			on_road.put(curr_wegiht)
			rw -= curr_wegiht
		else:
			on_road.put(0)
		sec += 1

	return sec + 1