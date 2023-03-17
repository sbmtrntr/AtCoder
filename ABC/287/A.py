N = int(input())
a = 0
for _ in range(N):
    S = input()
    if S[0] == 'A':
        a -= 1
    else:
        a += 1

if a > 0:
    print('Yes')
else:
    print('No')