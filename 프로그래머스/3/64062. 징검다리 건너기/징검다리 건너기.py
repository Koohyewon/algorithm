def solution(stones, k):
    left = 1
    right = max(stones)

    while left <= right:
        people = (left + right) // 2

        count = 0
        possible = True

        for stone in stones:
            if stone < people:
                count += 1
            else:
                count = 0

            if count >= k:
                possible = False
                break

        if possible:
            left = people + 1
        else:
            right = people - 1

    return right