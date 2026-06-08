def solution(storey):
    answer = 0

    while storey > 0:
        now = storey % 10
        next = (storey // 10) % 10

        if now < 5:
            answer += now
            storey //= 10

        elif now > 5:
            answer += 10 - now
            storey = storey // 10 + 1

        else: 
            answer += 5

            if next >= 5:
                storey = storey // 10 + 1
            else:
                storey //= 10

    return answer