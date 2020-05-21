import heapq


def solution(genres, plays):
	hash_table = {}
	for i, genre in enumerate(genres):
		if genre not in hash_table:
			hash_table[genre] = {
				'cnt': 0,
				'play_list': []
			}
		hash_table[genre]['cnt'] += plays[i]
		hash_table[genre]['play_list'].append((-plays[i], i))

	answer = []

	sorted_genres = sorted(hash_table.values(), key=lambda x: x['cnt'], reverse=True)
	for genre in sorted_genres:
		play_list = genre['play_list']
		heapq.heapify(play_list)
		if len(play_list) >= 2:
			answer.append(heapq.heappop(play_list)[1])
			answer.append(heapq.heappop(play_list)[1])
		else:
			answer.append(heapq.heappop(play_list)[1])

	return answer