def solution(id_list, report, k):
    report=list(set(report))

    cnt,mail = {},{}
    
    for name in id_list:
        cnt[name]=0
        mail[name]=0

    # 신고 횟수
    for i in report:
        _, target = i.split()
        cnt[target] += 1

    for i in report:
        user,target=i.split()

        if cnt[target] >= k:
            mail[user] += 1

    result = []

    for name in id_list:
        result.append(mail[name])

    return result