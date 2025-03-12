t = int(input())

for _ in range(t):
    n = int(input())
    cnt = {}
    team_list = list(map(int, input().split()))
    
    # 팀 주자 수
    for team in team_list:
        if team in cnt:
            cnt[team] += 1
        else:
            cnt[team] = 1
    
    # 6명 미만 제외
    del_team = {}
    for team in cnt:
        if cnt[team] < 6:
            del_team[team] = True
    
    team_score = {}
    rank = 1 
    
    for team in team_list:
        if team not in del_team:
            if team in team_score:
                if team_score[team]['top4'] < 4:
                    team_score[team]['top4'] += 1
                    team_score[team]['total_score'] += rank
                elif team_score[team]['top4'] == 4:
                    team_score[team]['top4'] += 1
                    team_score[team]['fifth'] = rank
            else:
                team_score[team] = {'top4': 1, 'total_score': rank, 'fifth': 0}
            
            rank += 1
    
    # 동점인 경우 다섯번째 주자 빨리들어온 순
    winner = sorted(team_score.items(), key=lambda x: (x[1]['total_score'], x[1]['fifth']))[0][0]
    print(winner)