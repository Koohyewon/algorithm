import sys

T = int(sys.stdin.readline()) 
for i in range(T):
    k = int(sys.stdin.readline())  
    n = int(sys.stdin.readline())  

    people = [[0] * (n + 1) for _ in range(k + 1)]  

    for j in range(1, n + 1):
        people[0][j] = j

    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            people[floor][room] = people[floor - 1][room] + people[floor][room - 1]

    print(people[k][n])