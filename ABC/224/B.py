h, w = map(int, input().split())

A = []

for i in range(h):
    A.append(list(map(int, input().split())))

for i1 in range(h):
    for i2 in range(h):
        for j1 in range(w):
            for j2 in range(w):
                if i1 < i2 and j1 < j2:
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print("No")
                        exit()
print('Yes')