H, W, X, Y = map(int, input().split())

masu = []
for i in range(H):
    masu.append(list(input()))

X -= 1
Y -= 1

ans = 1

#left
for i in range(Y):
    if masu[X][Y-i-1] == '.':
        ans += 1
    else:
        break

#right
for i in range(W-Y-1):
    if masu[X][Y+i+1] == ".":
        ans += 1
    else:
        break

#up
for i in range(X):
    if masu[X-i-1][Y] == ".":
        ans += 1
    else:
        break

#down
for i in range(H-X-1):
    if masu[X+i+1][Y] == ".":
        ans += 1
    else:
        break

print(ans)

