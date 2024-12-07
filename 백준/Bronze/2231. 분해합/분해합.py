import sys

n=int(sys.stdin.readline())

m_found=False

for i in range(1, n+1):
    m = i + sum(int(num) for num in str(i))
    if m == n:
        print(i)
        m_found = True
        break

if not m_found:
    print(0)