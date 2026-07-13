def solution(n):
    answer = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else: #홀수는 점프를 반드시 1회 해야함
            answer += 1
            n -= 1

    return answer