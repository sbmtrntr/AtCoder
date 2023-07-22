S = input()
ans = 0
flag = False
for i in range(len(S)-1):
    if flag:
        flag = False
        continue
    if S[i] == '0':
        if S[i+1] == '0':
            ans += 1
            flag = True
        else:
            ans += 1
    else:
        ans += 1

if flag:
    print(ans)
else:
    print(ans + 1)