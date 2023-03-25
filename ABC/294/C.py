N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
dic = {}
for i in range(N+M):
    dic[C[i]] = i+1
ans = []
for i in range(N):
    ans.append(dic[A[i]])
print(*ans)
ans = []
for i in range(M):
    ans.append(dic[B[i]])
print(*ans)