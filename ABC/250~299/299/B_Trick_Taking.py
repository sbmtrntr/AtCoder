N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

flag = False
value = 0
ans = 0
for i in range(N):
    if C[i] == T:
        flag = True

if flag:
    for i in range(N):
        if C[i] == T and value < R[i]:
            ans = i+1
            value = R[i]

else:
    for i in range(N):
        if C[i] == C[0] and value < R[i]:
            ans = i+1
            value = R[i]


print(ans)