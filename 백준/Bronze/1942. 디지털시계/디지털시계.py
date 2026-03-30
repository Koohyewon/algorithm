def check_three(h, m, s):
    #각 자리 숫자 합이 3의 배수인지
    return 1 if (h//10 + h%10 + m//10 + m%10 + s//10 + s%10) % 3 == 0 else 0

for _ in range(3):
    start, end = input().split()
    sh, sm, ss = map(int, start.split(':'))
    eh, em, es = map(int, end.split(':'))

    count = 0

    while True:
        count += check_three(sh, sm, ss)

        if (sh == eh) and (sm == em) and (ss == es):
            break

        ss += 1

        if ss == 60:
            ss = 0
            sm += 1
        
        if sm == 60:
            sm = 0
            sh += 1

        if sh == 24:
            sh = 0

    print(count)