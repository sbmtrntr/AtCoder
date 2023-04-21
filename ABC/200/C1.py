N = int(input())
A = list(map(int, input().split()))

group = [0]*200

for i in range(N):
    group[A[i]%200] += 1

ans = 0

for i in range(200):
    ans += group[i]*(group[i]-1)//2

print(ans)
