def is_prime(num):
    if num < 2:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def solution(n, k):
    # n을 k진수로 변환
    converted = ""

    while n > 0:
        converted = str(n % k) + converted
        n //= k

    # 0을 기준으로 숫자를 나눔
    numbers = converted.split("0")

    answer = 0

    for num in numbers:
        # 0 때문에 생긴 빈 문자열은 제외
        if num == "":
            continue

        # 10진수로 변환해서 소수인지 확인
        if is_prime(int(num)):
            answer += 1

    return answer