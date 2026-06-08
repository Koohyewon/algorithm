def solution(players, callings):
    rank = {}

    idx = 0
    for i in players:
        rank[i]=idx; idx+=1

    for name in callings:
        temp=rank[name]
        players[temp], players[temp-1] = players[temp-1], players[temp]

        rank[name] -= 1              
        rank[players[temp]] += 1     

    return players