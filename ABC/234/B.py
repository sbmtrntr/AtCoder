import math

N = int(input())

zahyo = []

for i in range(N):
    zahyo.append(tuple(map(int, input().split())))

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        distance = math.sqrt((zahyo[i][0] - zahyo[j][0])**2 + (zahyo[i][1] - zahyo[j][1])**2)
        ans = max(ans, distance)

print(ans)