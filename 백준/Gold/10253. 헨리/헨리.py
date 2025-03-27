def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input()) 

for _ in range(t):
    a, b = map(int, input().split()) 

    while a != 1:
        x = b // a + 1 
        denominator = lcm(b, x) 
        frac1 = denominator // x  
        frac2 = denominator // b 

        a = a * frac2 - frac1
        b = denominator

        check = gcd(a, b)
        if check != 1: 
            a //= check
            b //= check
    
    print(b)  