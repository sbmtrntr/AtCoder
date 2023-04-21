S = input()

flag = True

for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if S[i] == S[j]:
           flag = False

Flag1 = False
Flag2 = False

for i in range(len(S)):
    if S[i].isupper():
        Flag1 = True
    if S[i].islower():
        Flag2 = True

if flag and Flag1 and Flag2:
    print('Yes')
else:
    print('No')

    