def solution(n, lost, reserve):
	cnt = [1 for _ in range(n)]
	for l in lost:
		cnt[l - 1] -= 1
	for r in reserve:
		cnt[r - 1] += 1

	for i in range(n):
		if cnt[i] == 2:
			if i >= 1 and cnt[i - 1] == 0:
				cnt[i - 1] += 1
				cnt[i] -= 1
			elif i <= n - 2 and cnt[i + 1] == 0:
				cnt[i + 1] += 1
				cnt[i] -= 1

	return len(list(filter(None, cnt)))