def solution(n):
    target = 0          # n의 1의 개수 
    tmp = n
    while tmp > 0:
        if tmp % 2 == 1:
            target = target + 1
        tmp = tmp // 2

    num = n + 1
    while True:
        count = 0       # num의 1의 개수
        tmp = num
        while tmp > 0:
            if tmp % 2 == 1:
                count = count + 1
            tmp = tmp // 2

        if count == target:
            return num

        num = num + 1