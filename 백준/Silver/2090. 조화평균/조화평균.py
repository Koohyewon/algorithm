def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

n = int(input())
numbers = list(map(int, input().split()))

top = get_product(numbers)
bottom = sum(top // num for num in numbers) 

gcd_value = get_gcd(bottom, top)
bottom //= gcd_value
top //= gcd_value

print(f"{top}/{bottom}")