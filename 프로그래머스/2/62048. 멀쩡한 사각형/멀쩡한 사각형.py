def solution(w, h):
    a, b = w, h
    while b:
        a, b = b, a%b
    return w*h - (w+h-a)