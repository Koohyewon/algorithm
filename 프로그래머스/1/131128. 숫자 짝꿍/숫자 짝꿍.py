def solution(X, Y):
    count_x = [0] * 10
    count_y = [0] * 10

    for c in X:
        count_x[int(c)] = count_x[int(c)] + 1

    for c in Y:
        count_y[int(c)] = count_y[int(c)] + 1

    tmp = []

    for num in range(9, -1, -1):
        if count_x[num] < count_y[num]:
            cnt = count_x[num]
        else:
            cnt = count_y[num]

        for i in range(cnt):
            tmp.append(str(num))

    answer = "".join(tmp)

    if answer == "":
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer