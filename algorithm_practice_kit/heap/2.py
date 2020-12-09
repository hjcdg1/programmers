import heapq


def solution(jobs):
	N = len(jobs)
	jobs = [[job[1], job[0]] for job in jobs]
	jobs.sort(key=lambda x: x[1])

	idx = 0
	start = 0
	total_wait_time = 0
	job_cnt = 0

	h = []

	while True:
		while idx < N and jobs[idx][1] <= start:
			heapq.heappush(h, jobs[idx])
			idx += 1

		if not h:
			start = jobs[idx][1]
			continue

		min_job = heapq.heappop(h)

		start += min_job[0]
		total_wait_time += start - min_job[1]
        
		job_cnt += 1
		if job_cnt == N:
			break

	answer = total_wait_time // N
	return answer