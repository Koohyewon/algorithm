def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):          # 결과의 행 = arr1의 행
        row = []
        for j in range(len(arr2[0])):   # 결과의 열 = arr2의 열
            # arr1의 i번째 행과 arr2의 j번째 열을 같은 위치끼리 곱해서 더한다
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            row.append(total)
        answer.append(row)

    return answer