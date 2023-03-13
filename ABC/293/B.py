N = int(input())
called = set()
A = list(map(int, input().split()))
ans = []
for i in range(N):
    if i+1 not in called:
        called.add(A[i])

for i in range(1, N+1):
    if i not in called:
        ans.append(i)

print(len(ans))
print(*ans)