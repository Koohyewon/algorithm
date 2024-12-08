import sys

N, X, Y = map(int, sys.stdin.readline().split())
sandwiches = list(map(int, sys.stdin.readline().split()))

max_eat = 0
min_waste = 0

for sandwich in sandwiches:
    if sandwich < X:
        min_waste += sandwich
        continue

    eat = sandwich // X
    max_eat += eat
    waste = sandwich % X

    if waste > (Y - X) * eat:
        min_waste += waste - ((Y - X) * eat)

print(max_eat)
print(min_waste)