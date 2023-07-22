N, X = map(int, input().split())
a = []
ans = 0
l = 1
for i in range(N):
    temp = list(map(int, input().split()))
    l *= temp[0]
    a.append(temp[1:])

for i in range(l):
    seki = 1
    ind = i
    for x in a:
        seki *= x[ind % len(x)]
        ind //= len(x)
        if seki > X:
            break
        
    if seki == X:
        ans += 1


print(ans)