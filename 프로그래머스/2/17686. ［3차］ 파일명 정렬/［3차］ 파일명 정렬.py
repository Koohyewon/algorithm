def get_key(item):
    return (item[0].lower(), int(item[1]))


def solution(files):
    parsed = []

    for f in files:
        head = ""
        number = ""
        i = 0
        
        while i < len(f):
            if f[i].isdigit():
                break
            head = head + f[i]
            i = i + 1

        while i < len(f):
            if not f[i].isdigit():
                break
            number = number + f[i]
            i = i + 1
            if len(number) == 5:
                break

        parsed.append([head, number, f])

    parsed.sort(key=get_key)

    answer = []
    for p in parsed:
        answer.append(p[2])

    return answer