A, B = map(int,input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

if B > A:
    A, B = B, A

print(A*B // gcd(A, B))