def solution(name):
    ans = 0
    move = len(name) - 1

    for i in range(len(name)):
        ans += min(ord(name[i]) - ord('A'),
                   ord('Z') - ord(name[i]) + 1)

        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1

        move = min(move,
                   i * 2 + len(name) - j,
                   (len(name) - j) * 2 + i)

    return ans + move