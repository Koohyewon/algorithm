def solution(video_len, pos, op_start, op_end, commands):

    def second(time):
        mm, ss = map(int, time.split(":"))
        return mm * 60 + ss

    def time(second):
        mm = second // 60
        ss = second % 60

        if mm < 10:
            mm = "0" + str(mm)
        else:
            mm = str(mm)

        if ss < 10:
            ss = "0" + str(ss)
        else:
            ss = str(ss)

        return mm + ":" + ss

    video_len = second(video_len)
    pos = second(pos)
    op_start = second(op_start)
    op_end = second(op_end)

    for command in commands:

        if op_start <= pos <= op_end:
            pos = op_end

        if command == "prev":
            pos = max(0, pos - 10)
        else:
            pos = min(video_len, pos + 10)

        if op_start <= pos <= op_end:
            pos = op_end

    return time(pos)