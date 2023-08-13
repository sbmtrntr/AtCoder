N = int(input())
A = list(map(int,input().split()))
accum = [0]*(N+1)
for i in range(N):
    if A[i]:
        accum[i+1] = accum[i] + A[i]
    else:
        accum[i+1] = accum[i] - 1

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    if accum[r] - accum[l-1] > 0:
        print('win')
    elif accum[r] - accum[l-1] == 0:
        print('draw')
    else:
        print('lose')