N, W = map(int, input().split())
accum = [0]*(2*10**5 + 1)

for i in range(N):
    s, t, p = map(int, input().split())
    accum[s] += p
    accum[t] -= p

for i in range(2*10**5):
    accum[i+1] += accum[i]

if max(accum) <= W:
    print('Yes')
else:
    print('No')