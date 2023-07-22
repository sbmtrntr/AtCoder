N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
count_x = [0]*N
count_a = [0]*N

for i in range(N):
    count_x[B[C[i]-1]-1] += 1
    count_a[A[i-1]-1] += 1
    
for i in range(N):
    ans += count_x[i]*count_a[i]

print(ans)