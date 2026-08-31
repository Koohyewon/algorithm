def solution(n, k):
    # k진수로 변환
    result = ""
    while n > 0:
        result = str(n % k) + result
        n //= k

    # 0을 기준으로 나누기
    arr = result.split("0")
    answer = 0

    for x in arr:
        if x == "":
            continue
        if is_prime(int(x)):
            answer += 1
    return answer


def is_prime(x):
    if x < 2:
        return False
    i = 2

    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True