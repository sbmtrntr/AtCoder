A, B = map(int,input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

if A < B:
    A, B = B, A

print(gcd(A, B))