def solution(elements):
    n = len(elements)

    arr = elements + elements

    result = set()

    for start in range(n):
        total = 0
        for length in range(n):
            total = total + arr[start + length]
            result.add(total)

    return len(result)