def can_cut_trees(heights, H, M):
    total_length = 0
    for height in heights:
        if height > H:
            total_length += height - H
    return total_length >= M

def find_max_height(N, M, heights):
    low, high = 0, max(heights)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_cut_trees(heights, mid, M):
            result = mid  
            low = mid + 1
        else:
            high = mid - 1

    return result

N, M = map(int, input().split())
heights = list(map(int, input().split()))

print(find_max_height(N, M, heights))
