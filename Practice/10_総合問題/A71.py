N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
A.sort()
B.sort()
for i in range(N):
    ans += A[i]*B[N-i-1]

print(ans)