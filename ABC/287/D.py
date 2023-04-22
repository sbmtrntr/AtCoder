S = input()
T = input()

for x in range(len(T)+1):
    print(S[:x] + S[len(S)-(len(T)-x):])
