def solution(topping):
    answer = 0

    right = {}

    # 오른쪽 토핑 개수 저장
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1

    left = set()

    for t in topping:
        left.add(t)

        right[t] -= 1

        if right[t] == 0:
            del right[t]

        if len(left) == len(right):
            answer += 1

    return answer