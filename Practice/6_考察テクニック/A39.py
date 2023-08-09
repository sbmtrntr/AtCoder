N = int(input())
time = []
for i in range(N):
    l, r = map(int,input().split())
    time.append((r, l))

time.sort()
ans = 0
now = 0
for i in range(N):
    if now <= time[i][1]:
        ans += 1
        now = time[i][0]

print(ans)