n, r = map(int,input().split())
mod = 10**9 + 7

bunshi = 1
for i in range(1, n+1):
    bunshi = bunshi * i % mod

bunbo = 1
for i in range(1, r+1):
    bunbo = bunbo * i % mod
    
for i in range(1, n-r+1):
    bunbo = bunbo * i % mod

