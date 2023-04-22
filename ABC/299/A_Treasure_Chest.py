N = int(input())
S = input()
cnt = 0
for i in range(N):
    if S[i] == '|':
        cnt += 1
    if S[i] == '*':
        if cnt == 1:
            exit(print('in'))
        else:
            exit(print('out'))