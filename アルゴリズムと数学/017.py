n = int(input())

A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a* b // gcd(a, b)

ans = lcm(A[0], A[1])

for i in range(2, n):
    ans = (ans)

