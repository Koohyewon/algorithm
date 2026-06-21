def solution(want, number, discount):
    answer = 0

    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for s in range(len(discount) - 9):
        sale_dic = {}

        for i in range(s, s + 10):
            item = discount[i]

            if item in sale_dic:
                sale_dic[item] += 1
            else:
                sale_dic[item] = 1

        if sale_dic == want_dic:
            answer += 1

    return answer