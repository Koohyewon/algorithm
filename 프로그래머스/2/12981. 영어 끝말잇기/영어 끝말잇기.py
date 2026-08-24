def solution(n, words):
    used = set()

    for i in range(len(words)):
        if i > 0 and words[i][0] != words[i - 1][-1]:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]

        if words[i] in used:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]

        used.add(words[i])

    return [0, 0]