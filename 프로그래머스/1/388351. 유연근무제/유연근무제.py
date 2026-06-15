def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        hope_time = schedules[i]

        h = hope_time//100
        m = hope_time%100
        m += 10

        if m >= 60:
            h += 1; m -= 60

        hope_time = h*100+m

        success=True
        for j in range(7):
            day = (startday+j-1)%7+1

            if day == 6 or day == 7: continue    #토일 제외

            if timelogs[i][j] > hope_time:
                success=False
                break

        if success: answer += 1

    return answer