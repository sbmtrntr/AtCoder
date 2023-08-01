N = int(input())
S = input()
flag1, flag2, flag3 = False, False, False
for i in range(N):
    if S[i] == 'A':
        flag1 = True
    if S[i] == 'B':
        flag2 = True
    if S[i] == 'C':
        flag3 = True
    if flag1 and flag2 and flag3:
        print(i+1)
        break