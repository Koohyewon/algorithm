def solution(scores):
    wanho_a = scores[0][0]
    wanho_b = scores[0][1]
    wanho_sum = wanho_a + wanho_b

    # a는 높은 순, b는 낮은 순으로 정렬하기 위해 a에 -를 붙여 저장한다
    people = []
    for a, b in scores:
        people.append([-a, b])
    people.sort()

    max_b = 0  # 지금까지 나온 동료 평가 점수 중 가장 큰 값
    rank = 1
    for minus_a, b in people:
        a = -minus_a

        # 앞에 a도 b도 더 높은 사원이 있으면 인센티브를 못 받는다
        if b < max_b:
            # 완호와 점수가 같은 사원이 걸러지면 완호도 못 받는다
            if a == wanho_a and b == wanho_b:
                return -1
            continue

        max_b = b

        # 완호보다 점수 합이 큰 사원 수만큼 석차가 밀린다
        if a + b > wanho_sum:
            rank += 1

    return rank