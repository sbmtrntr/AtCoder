N, S = map(int,input().split())
A = list(map(int,input().split()))

dp = [[0]*S for _ in range(N)]

for i in range(N):
    for j in range(S):
        