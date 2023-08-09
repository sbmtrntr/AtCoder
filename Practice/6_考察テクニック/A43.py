N, L = map(int,input().split())
A, B = [], []
for i in range(N):
    a, b = input().split()
    a = int(a)
    A.append(a)
    B.append(b)

mid = L // 2
ans = 0

for i in range(N):
    if B[i] == "E":
        ans = max(ans, L - A[i])
    else:
        ans = max(ans, L - A[i] + mid)

print(ans)