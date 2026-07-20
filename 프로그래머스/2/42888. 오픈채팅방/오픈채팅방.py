def solution(record):
    nickname = {}

    for r in record:
        info = r.split()

        if info[0] == "Enter":
            nickname[info[1]] = info[2]

        elif info[0] == "Change":
            nickname[info[1]] = info[2]

    answer = []

    for r in record:
        info = r.split()

        if info[0] == "Enter":
            answer.append(f"{nickname[info[1]]}님이 들어왔습니다.")

        elif info[0] == "Leave":
            answer.append(f"{nickname[info[1]]}님이 나갔습니다.")

    return answer