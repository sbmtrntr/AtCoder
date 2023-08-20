N = int(input())
FS = []
for i in range(N):
    f, s = map(int, input().split())
    FS.append([s, f])
FS.sort(reverse=True)
ans = FS[0][0]
for i in range(1, N):
    if FS[i][1] == FS[0][1]:
        ans = max(ans, FS[0][0] + FS[i][0] // 2)
    else:
        ans = max(ans, FS[0][0] + FS[i][0])
print(ans)