S = input()

X = []

for i in range(4):
    X.append(int(S[i]))


if len(set(X)) == 1:
    print("Weak")
    exit()

for i in range(3):
    if X[i] != 9:
        if X[i+1] != X[i]+1:
            print("Strong")
            exit()
    else:
        if X[i+1] != 0:
            print("Strong")
            exit()

print("Weak")