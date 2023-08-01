from math import gcd

A, B = map(int, input().split())

ans = A*B//gcd(A, B)

if ans > 10**18:
    print('Large')
else:
    print(ans)