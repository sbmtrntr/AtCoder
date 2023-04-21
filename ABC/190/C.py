N, M = map(int, input().split())
A, B = [0]*M, [0]*M

for i in range(M):
    A[i], B[i] = map(int, input().split())

K = int(input())
C, D = [0]*K, [0]*K

for i in range(K):
    C[i], D[i] = map(int, input().split())

ans = 0
for i in range(2**K+1):
    b = bin(i)[2:]
    if len(b) != K:
        b = "0"*(K-len(b)) + b
    temp = [False]*N
    for j in range(K):
        if b[j] == "0":
            temp[C[j]-1] = True
        else:
            temp[D[j]-1] = True
    temp_ans = 0
    for j in range(M):
        if temp[A[j]-1] and temp[B[j]-1]:
            temp_ans += 1
    ans = max(ans, temp_ans)

print(ans)
