def solution(N, stages):
    stage = [0]*(N + 2)

    for s in stages:
        stage[s] += 1

    clear = stage[-1]

    for i in range(N, 0, -1):
        now = stage[i]

        if clear+now != 0:
            stage[i] = now/(clear+now)
        else:
            stage[i] = 0

        clear += now

    fail=[]

    for i in range(1, N + 1):
        fail.append((-stage[i], i))

    fail.sort()

    answer=[]

    for rate, num in fail:
        answer.append(num)

    return answer