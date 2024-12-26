def zero_count(N):
    count = 0
    while N >= 5:
        N //= 5
        count += N
    return count

def find_minimum_N(M):
    left, right = 0, 5 * M
    
    while left <= right:
        mid = (left + right) // 2
        count = zero_count(mid)
        
        if count < M:
            left = mid + 1
        elif count > M:
            right = mid - 1
        else:
            if zero_count(mid - 1) < M:
                return mid
            right = mid - 1
    
    return -1

M = int(input().strip())

print(find_minimum_N(M))
