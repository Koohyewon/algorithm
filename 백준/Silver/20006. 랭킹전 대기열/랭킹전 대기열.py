import sys
input=sys.stdin.readline

p, m = map(int, input().split())
players = []

for _ in range(p):
    l, n = input().split()
    l = int(l)
    players.append((l, n))

rooms = []

for level, name in players:
    match_room = None
    for room in rooms:
        if room["min_level"] <= level <= room["max_level"] and len(room["players"]) < m:
            match_room = room
            break

    if match_room:
        match_room["players"].append((level, name))
    else:
        new_room = {
            "min_level": level - 10,
            "max_level": level + 10,
            "players": [(level, name)]
        }
        rooms.append(new_room)


for room in rooms:
    if len(room["players"]) == m:
        print("Started!")
    else:
        print("Waiting!")
        
    for player in sorted(room["players"], key=lambda x: x[1]):
        print(player[0], player[1])        
