def solution(clothes):
    answer = 1
    dic = {}

    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1

    for i in dic:
        answer *= (dic[i] + 1)

    return answer - 1