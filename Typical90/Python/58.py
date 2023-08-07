from collections import defaultdict
N, K = map(int, input().split())
mod = 10**5
memo = defaultdict(int)
cnt = 0

while N not in memo and K > 0:
    memo[N] = cnt
    N = str(N)
    y = 0
    for n in N:
        y += int(n)
    N = (int(N) + y) % mod
    cnt += 1
    K -= 1

if K == 0:
    print(N)
else:
    K %= cnt - memo[N]
    for _ in range(K):
        N = str(N)
        y = 0
        for n in N:
            y += int(n)
        N = (int(N) + y) % mod
    print(N)