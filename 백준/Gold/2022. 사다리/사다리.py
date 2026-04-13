def get_c(x, y, w):
    h1 = (x*x - w*w) ** 0.5
    h2 = (y*y - w*w) ** 0.5
    return (h1 * h2) / (h1 + h2)


x, y, c = map(float, input().split())

left = 0
right = min(x, y)

while right - left > 0.0001:
    mid = (left + right) / 2

    if get_c(x, y, mid) > c:
        left = mid
    else:
        right = mid

print(round(right, 3))