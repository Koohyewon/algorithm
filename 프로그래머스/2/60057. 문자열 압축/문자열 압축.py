def solution(s):
    answer = len(s)

    for n in range(1, len(s) // 2 + 1):    # 자르는 단위 n

        cur_s = ""
        
        temp = s[0:n]
        cnt = 1

        for i in range(n, len(s), n):
            current = s[i:i+n]

            if temp == current:
                cnt += 1

            else:
                if cnt > 1:
                    cur_s += str(cnt) + temp
                else:
                    cur_s += temp

                temp = current
                cnt = 1

        if cnt > 1:
            cur_s += str(cnt) + temp
        else:
            cur_s += temp

        answer = min(answer, len(cur_s))

    return answer