N = int(input())

A = list(map(int, input().split()))

ans = 0
x = [0]*200

for i in range(N):
    x[A[i] % 200] = x[A[i] % 200] + 1

for i in range(200):
    ans += x[i]*(x[i]-1)//2
 
print(ans)
