N, L, R = map(int, input().split())
A = list(map(int, input().split()))

accum = [0]*N
accum[0] = A[0]
for i in range(1, N):
    accum[i] = accum[i-1] + A[i]

accum_rev = [0]*N
accum_rev[0] = A[-1]
for i in range(1, N):
    accum_rev[i] = accum_rev[i-1] + A[N-i-1]

ans = 10**20
x = 0
y = 0

for i in range(N):
    if accum[i] >= L*(i+1):
        x = i + 1
    else:
        break

for i in range(N):
    if accum_rev[i] >= R*(i+1):
        y = i + 1
    else:
        break
print(x, y)
print(L*x + accum[N-y-1] - accum[x] + R*y)


        
