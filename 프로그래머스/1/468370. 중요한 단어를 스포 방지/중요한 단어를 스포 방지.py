def solution(message, spoiler_ranges):
    n = len(message)

    spoiler = [-1] * n

    for idx, (start, end) in enumerate(spoiler_ranges):
        for i in range(start, end + 1):
            spoiler[i] = idx

    normal_words = set()

    opened = [[] for _ in range(len(spoiler_ranges))]

    i = 0

    while i < n:
        if message[i] == " ":
            i += 1
            continue

        start = i

        while i < n and message[i] != " ":
            i += 1

        end = i - 1
        word = message[start:i]

        last_click = -1

        for pos in range(start, end + 1):
            if spoiler[pos] != -1:
                last_click = max(last_click, spoiler[pos])

        if last_click == -1:
            normal_words.add(word)
        else:
            opened[last_click].append(word)

    answer = 0
    seen = set()

    for words in opened:
        for word in words:
            if word not in normal_words and word not in seen:
                answer += 1

            seen.add(word)

    return answer