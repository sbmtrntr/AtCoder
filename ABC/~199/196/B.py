X = input()

for i in range(len(X)):
    if X[i] == ".":
        print(X[:i])
        exit()

print(X)