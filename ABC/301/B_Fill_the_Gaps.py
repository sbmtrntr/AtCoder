N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    if abs(A[i] - A[i+1]) == 1:
        ans.append(A[i])
    else:
        if A[i] < A[i+1]:
            for j in range(A[i], A[i+1]):
                ans.append(j)
        else:
            for j in range(A[i], A[i+1], -1):
                ans.append(j)

ans.append(A[-1])
print(*ans)