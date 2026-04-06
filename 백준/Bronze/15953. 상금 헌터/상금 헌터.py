# 1회 (등수 범위, 상금)
prize1 = [
    (1, 1, 5000000),
    (2, 3, 3000000),
    (4, 6, 2000000),
    (7, 10, 500000),
    (11, 15, 300000),
    (16, 21, 100000),
]

# 2회
prize2 = [
    (1, 1, 5120000),
    (2, 3, 2560000),
    (4, 7, 1280000),
    (8, 15, 640000),
    (16, 31, 320000),
]

T = int(input())

def get_result(rank, prize_list):
    if rank==0:
        return 0
    for start, end, money in prize_list:
        if start<=rank<=end:
            return money        
    return 0

for i in range(T):
    a,b=map(int, input().split())
    result = get_result(a, prize1) + get_result(b, prize2)
    print(result)