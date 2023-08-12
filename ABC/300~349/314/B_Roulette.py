N = int(input())
A = []
C = []
for i in range(N):
    C.append(int(input()))
    A.append(set(map(int, input().split())))

X = int(input())
ans = []
cnt = 10**10
for i in range(N):
    if X in A[i] and cnt > C[i]:
        cnt = C[i]
        ans = []
        ans.append(i+1)
    elif X in A[i] and cnt == C[i]:
        ans.append(i+1)

ans.sort()
print(len(ans))
print(*ans)