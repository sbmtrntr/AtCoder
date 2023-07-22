S = input()
T = input()

for i in range(len(T)-1):
    if T[i] != S[i]:
        print(i+1)
        exit()

print(len(T))