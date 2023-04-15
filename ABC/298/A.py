N = int(input())
S = input()
cnt = 0
for i in range(N):
    if S[i] == 'x':
        exit(print('No'))
    if S[i] == 'o':
        cnt += 1

if cnt >= 1:
    print('Yes')
else:
    print('No')
    