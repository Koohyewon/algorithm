def solution(sizes):
    w = 0
    h = 0
    for a, b in sizes:
        if a < b: a, b = b, a
        if a > w: w = a
        if b > h: h = b

    return w * h