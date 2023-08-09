N, K = map(int,input().split())
A, B = [0]*N, [0]*N
for i in range(N):
    A[i], B[i] = map(int,input().split())

ans = 0

for i in range(1, 101):
    for j in range(1, 101):
        temp = 0
        for k in range(N):
            if 0 <= A[k] - i <= K and 0 <= B[k] - j <= K:
                temp += 1

        ans = max(ans, temp)

print(ans)