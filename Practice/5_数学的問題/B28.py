N = int(input())
mod = 10**9 + 7
a = [0]*N
a[0] = 1
a[1] = 1
for n in range(2, N):
    a[n] = (a[n-1] + a[n-2]) % mod

print(a[-1])