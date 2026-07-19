def solution(numbers):
    answer = []

    for number in numbers:
        b = list('0' + bin(number)[2:])

        for i in range(len(b) - 1, -1, -1):
            if b[i] == '0':
                b[i] = '1'
                if i != len(b) - 1:
                    b[i + 1] = '0'
                break

        answer.append(int(''.join(b), 2))

    return answer