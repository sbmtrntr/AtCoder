N, M = map(int, input().split())
cnt = [0]*N

for i in range(M):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1

print(cnt.index(max(cnt))+1)