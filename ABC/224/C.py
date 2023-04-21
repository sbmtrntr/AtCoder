N = int(input())

zahyo = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if (zahyo[i][0] - zahyo[k][0])*(zahyo[j][1] - zahyo[k][1]) - (zahyo[j][0] - zahyo[k][0])*(zahyo[i][1] - zahyo[k][1]) != 0:
                ans += 1
print(ans)
