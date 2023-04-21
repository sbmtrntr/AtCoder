S = input()
T = input()

sa = (ord(S[0]) - ord(T[0])) % 26

for i in range(len(S)):
    if sa != (ord(S[i]) - ord(T[i])) % 26:
        print('No')
        exit()

print('Yes')