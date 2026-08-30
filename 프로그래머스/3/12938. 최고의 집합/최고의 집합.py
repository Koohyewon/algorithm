def solution(n, s):
    if s < n:
        return [-1]

    num = s // n
    rest = s % n

    answer = [num] * n

    for i in range(rest):
        answer[i] += 1

    answer.sort()

    return answer