def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(signals):
    period = 1

    for green, yellow, red in signals:
        cycle = green + yellow + red
        period = lcm(period, cycle)

    for time in range(1, period + 1):
        all_yellow = True

        for green, yellow, red in signals:
            cycle = green + yellow + red
            current = (time - 1) % cycle

            if not (green <= current < green + yellow):
                all_yellow = False
                break

        if all_yellow:
            return time

    return -1