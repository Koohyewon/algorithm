def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

# 입력 처리
n, m = map(int, input().split())
temp = list(map(int, input().split()))
truth_known = temp[1:]  # 진실을 아는 사람들

parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

# 유니온 파인드 초기화
parent = [i for i in range(n + 1)]

# 파티 구성원들을 서로 연결
for party in parties:
    for i in range(1, len(party)):
        union(party[0], party[i])

# 진실을 아는 사람의 루트를 찾는다
truth_roots = set(find(person) for person in truth_known)

# 각 파티에 대해 진실을 아는 사람이 포함되어 있는지 확인
count = 0
for party in parties:
    if all(find(person) not in truth_roots for person in party):
        count += 1

print(count)