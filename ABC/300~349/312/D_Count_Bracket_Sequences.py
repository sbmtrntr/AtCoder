S = input()
mod = 998244353
N = len(S)

dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i] == '(':
            
