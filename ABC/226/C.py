N = int(input())

T, K, A = [], [], []

for i in range(N):
    temp = list(map(int, input().split()))
    T.append(temp[0])
    K.append(temp[1])
    A.append(temp[2:])

shutoku = [False] * N
shutoku[-1] = True
ans = 0

for i in range(N-1, -1, -1):
    if not shutoku[i]:
        continue
    else:
        for j in A[i]:
            j -= 1
            shutoku[j] = True

for i in range(N):
    if shutoku[i]:
        ans += T[i]

print(ans)
