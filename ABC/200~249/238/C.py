N = int(input())

ans = 0
for i in range(18):
    if N < 10**i:
        break
    
    k = min(10**(i+1)-1, N) - 10**i + 1
    ans += k*(k+1)//2
    ans %= 998244353

print(ans)

