def find_y(x, k):
    result = 0
    bit_position = 0

    while k > 0:
        if (x & (1 << bit_position)) == 0:
            if k & 1:
                result |= (1 << bit_position)
            k >>= 1
        bit_position += 1

    return result

x, k = map(int, input().split())
y = find_y(x, k)
print(y)