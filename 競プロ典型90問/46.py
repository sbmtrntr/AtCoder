N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Agruops = [[]for _ in range(46)]
Bgruops = [[]for _ in range(46)]
Cgruops = [[]for _ in range(46)]

for i in range(N):
    Agruops[A[i]%46].append(A[i])
    Bgruops[B[i]%46].append(B[i])
    Cgruops[C[i]%46].append(C[i])

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + k + j) % 46 == 0:
                ans += len(Agruops[i])*len(Bgruops[j])*len(Cgruops[k])

print(ans)

