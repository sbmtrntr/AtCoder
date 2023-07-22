N = int(input())
P = list(map(int, input().split()))

Q = [0]*N

for i in range(N):
    Q[(i - P[i]) % N] += 1
    Q[(i+1 - P[i]) % N] += 1
    Q[(i-1 - P[i]) % N] += 1

print(max(Q))