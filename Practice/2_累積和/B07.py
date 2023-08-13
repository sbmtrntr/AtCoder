T = int(input())
N = int(input())
accum = [0]*(T+1)
for i in range(N):
    l, r = map(int,input().split())
    accum[l] += 1
    accum[r] -= 1

for i in range(T):
    accum[i+1] += accum[i]

for i in range(T):
    print(accum[i])