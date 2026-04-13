S=input().strip()

zero=S.count("0")
one=S.count("1")

Thanos_zero=zero//2
Thanos_one=one//2

result="0"*Thanos_zero+"1"*Thanos_one

print(result)
