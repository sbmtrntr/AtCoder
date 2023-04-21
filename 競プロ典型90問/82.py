L, R = map(int, input().split())
MOD = 10**9 + 7

def f(a, b):
    if a > b:
        return 0
    else:
        return (a+b)*(b-a+1)//2

ans = 0
for i in range(1, 20):
    l, r = 10**(i-1), 10**i-1
    ans += i * f(max(l, L), min(r, R))
    ans %= MOD

print(ans)