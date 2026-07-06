def change2(num, n):    #이진변환 binary가 생각이 안나서리...
    result = ""

    while num > 0:
        result = str(num % 2) + result
        num //= 2

    while len(result) < n:
        result = "0" + result

    return result

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = change2(arr1[i], n)
        b = change2(arr2[i], n)

        row = ""

        for j in range(n):
            if a[j] == "1" or b[j] == "1":
                row += "#"
            else:
                row += " "

        answer.append(row)

    return answer