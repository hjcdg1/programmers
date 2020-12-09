import math


def solution(progresses, speeds):
	N = len(progresses)

	# 개발 소요 기간
	required_days = []
	required_days_cnt = []
	for i in range(N):
		progress = progresses[i]
		speed = speeds[i]
		required_day = int(math.ceil((100 - progress) / speed))

		if not required_days or required_days[-1] < required_day:
			required_days.append(required_day)
			required_days_cnt.append(1)
		else:
			required_days_cnt[-1] += 1

	return required_days_cnt