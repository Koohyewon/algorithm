def solution(n):
    answer = ""

    while n > 0:
        if n % 3 == 1:
            answer = "1" + answer
        elif n % 3 == 2:
            answer = "2" + answer
        else:
            answer = "4" + answer
            n = n - 1       # 4는 3을 대신하므로 한 칸 당겨준다

        n = n // 3

    return answer