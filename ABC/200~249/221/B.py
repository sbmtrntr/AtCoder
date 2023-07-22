S = input()
T = input()

if S == T:
    print("Yes")
    exit()

for i in range(len(S)-1):
    swap_S = ""
    swap_S = S[:i] + S[i+1] + S[i] + S[i+2:]
    if swap_S == T:
        print('Yes')
        exit()

print("No")