def solution(fees, records):
    base_time = fees[0]    # 기본 시간(분)
    base_fee = fees[1]     # 기본 요금(원)
    unit_time = fees[2]    # 단위 시간(분)
    unit_fee = fees[3]     # 단위 요금(원)

    in_time = {}   # 지금 주차장 안에 있는 차 -> 입차 시각(분)
    total = {}     # 차량번호 -> 누적 주차 시간(분)

    for record in records:
        temp = record.split(" ")
        time = temp[0]
        car = temp[1]
        state = temp[2]

        # 07:59 -> 479분
        hour = int(time[0:2])
        minute = int(time[3:5])
        now = hour * 60 + minute

        if state == "IN":
            in_time[car] = now
        else:
            stay = now - in_time[car]
            if car in total:
                total[car] = total[car] + stay
            else:
                total[car] = stay
            del in_time[car]   # 나갔으니까 주차장에서 지움

    # 아직 안 나간 차들은 23:59에 나간 걸로 침
    last_time = 23 * 60 + 59
    for car in in_time:
        stay = last_time - in_time[car]
        if car in total:
            total[car] = total[car] + stay
        else:
            total[car] = stay

    car_list = []
    for car in total:
        car_list.append(car)
    car_list.sort()

    answer = []
    for car in car_list:
        t = total[car]
        if t <= base_time:
            fee = base_fee
        else:
            over = t - base_time
            if over % unit_time == 0:
                count = over // unit_time
            else:
                count = over // unit_time + 1   # 나누어떨어지지 않으면 올림
            fee = base_fee + count * unit_fee
        answer.append(fee)

    return answer