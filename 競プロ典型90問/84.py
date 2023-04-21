N = int(input())
S = input()

ans = N*(N+1)//2

if N == 1:
    print(0)
    exit()
    
l = []
pre = S[0]
cnt = 1
for i in range(1, N-1):
    if pre == S[i]:
        cnt += 1
    else:
        l.append(cnt)
        pre = S[i]
        cnt = 1

if S[N-1] == pre:
    cnt += 1
    l.append(cnt)
else:
    l.append(cnt)
    l.append(1)

for num in l:
    ans -= num*(num+1)//2

print(ans)    