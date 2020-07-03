import heapq

def solution(operations):
    max_h = []
    min_h = []

    is_deleted = [False for _ in range(1000000)]

    for idx, operation in enumerate(operations):
        op, data = tuple(operation.split())
        data = int(data)

        if op == 'I':
            heapq.heappush(max_h, (-data, idx))
            heapq.heappush(min_h, (data, idx))
        else:
            if not (max_h and min_h):
                continue

            if data == 1:
                is_deleted[heapq.heappop(max_h)[1]] = True
            else:
                is_deleted[heapq.heappop(min_h)[1]] = True

            while max_h and is_deleted[max_h[0][1]]:
                heapq.heappop(max_h)

            while min_h and is_deleted[min_h[0][1]]:
                heapq.heappop(min_h)

    if not (max_h and min_h):
        return [0, 0]
    else:
        return [-heapq.heappop(max_h)[0], heapq.heappop(min_h)[0]]