n, x, y = map(int, input().split())
lengths = list(map(int, input().split()))

max_length = max(lengths)
dp = [(0, max_length)] * (max_length + 1)

for remaining_length in range(max_length + 1):
    if remaining_length < x:
        dp[remaining_length] = (0, remaining_length)
    else:
        best_meals = 0
        min_waste = float('inf')
        
        for k in range(x, min(y + 1, remaining_length + 1)):
            next_meals, next_waste = dp[remaining_length - k]
            total_meals = 1 + next_meals
 
            if total_meals > best_meals or (total_meals == best_meals and next_waste < min_waste):
                best_meals = total_meals
                min_waste = next_waste

        if remaining_length < min_waste:
            min_waste = remaining_length
        
        dp[remaining_length] = (best_meals, min_waste)

total_meals = 0
total_waste = 0

for length in lengths:
    meals, waste = dp[length]
    total_meals += meals
    total_waste += waste

print(total_meals)
print(total_waste)
