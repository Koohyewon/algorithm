def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        g = gcd(answer, num)
        answer = answer * num // g

    return answer