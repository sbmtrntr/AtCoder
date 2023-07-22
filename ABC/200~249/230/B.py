S = input()

T = 'oxx'*5

for i in range(len(T)-len(S)):
    if S == T[i:len(S)+i]:
        print('Yes')
        exit()

print('No')


# S = input()
# T = "oxx" * 5
# print("Yes" if S in T else "No")
