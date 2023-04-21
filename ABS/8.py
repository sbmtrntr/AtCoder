N = int(input())

d = []
for i in range(N):
    d.append(int(input()))

d.sort()
ans = 1
for i in range(len(d)-1, 0, -1):
    if d[i] > d[i-1]: ans += 1
    elif d[i] == d[i-1]: continue
    else: break

print(ans)