N = int(input())
S = input()
ans = []
cnt = 0
for i in range(N):
    if S[i] == '(':
        cnt += 1
        ans.append(S[i])
    elif S[i] == ')' and cnt > 0:
        while ans[-1] != '(':
            ans.pop()
        ans.pop()
        cnt -= 1
    else:
        ans.append(S[i])
print(''.join(ans))