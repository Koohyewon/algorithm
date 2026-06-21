import heapq

def solution(jobs):
    n = len(jobs)

    arr = []

    for i in range(len(jobs)):
        s = jobs[i][0]
        l = jobs[i][1]

        arr.append((s, l, i))

    jobs = sorted(arr)

    heap = []
    time, idx, total = 0, 0, 0

    while idx < n or heap:
        while idx < n and jobs[idx][0] <= time:
            s, l, num = jobs[idx]
            heapq.heappush(heap, (l, s, num))
            idx += 1

        if heap:
            l, s, num = heapq.heappop(heap)

            time += l
            total += time - s

        else:
            time = jobs[idx][0]

    return total // n