N = int(input())

X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

S = input()

left_max = {}
right_min = {}

for i in range(N):
    if S[i] == "L":
        if Y[i] not in left_max:
            left_max[Y[i]] = X[i]
        else:
            if left_max[Y[i]] < X[i]:
                left_max[Y[i]] = X[i]
    
    else:
        if Y[i] not in right_min:
            right_min[Y[i]] = X[i]
        else:
            if right_min[Y[i]] > X[i]:
                right_min[Y[i]] = X[i]

    try:
        if left_max[Y[i]] > right_min[Y[i]]:
            print('Yes')
            exit()
    except KeyError:
        continue

print('No')

