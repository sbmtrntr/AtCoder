S = list(map(int, input().split()))
flag = True
for i in range(7):
    if S[i] > S[i+1]:
        flag = False

for i in range(8):
    if 100 > S[i] or 675 < S[i]:
        flag = False

    if S[i] % 25 != 0:
        flag = False

if flag:
    print('Yes')
else:
    print('No')