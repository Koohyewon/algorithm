def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    b_index = 0

    for a in A:
        while b_index < len(B) and B[b_index] <= a:
            b_index += 1

        if b_index == len(B):
            break

        answer += 1
        b_index += 1

    return answer