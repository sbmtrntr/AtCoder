N = int(input())
S = input()
ans = 0
temp = 0
for i in range(N):
    if S[i] == 'o':
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 0

temp = 0
for i in range(N):
    if S[N-i-1] == 'o':
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 0

if ans == 0:
    print(-1)
else:
    print(ans)