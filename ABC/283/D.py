S = input()
left = 0
box = set()
for i in range(len(S)):
    if S[i] == '(':
        left += 1
    elif S[i] == ')':
        box.clear()
    else:
        if S[i] in box:
            exit(print('No'))
        else:
            box.add(S[i])

print('Yes')