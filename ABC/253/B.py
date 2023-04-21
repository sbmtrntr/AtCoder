h, w = map(int, input().split())

s = []

for i in range(h):
    s.append(input())

masu = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            masu.append([i, j])

print(abs(masu[0][0] - masu[1][0]) + abs(masu[0][1] - masu[1][1]))