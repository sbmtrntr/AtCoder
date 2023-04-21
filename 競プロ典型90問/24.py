N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sa = 0

for i in range(N):
    sa += abs(A[i]-B[i])

if sa > K:
    print('No')
elif (K - sa) % 2 == 0:
    print('Yes')
else:
    print('No')