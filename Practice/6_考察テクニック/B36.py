N, K = map(int, input().split())
S = input()
cnt = [0, 0]

for i in range(N):
    if S[i] == '0':
        cnt[0] += 1
    else:
        cnt[1] += 1

if cnt[1] % 2 == K % 2:
    print('Yes')
else:
    print('No')