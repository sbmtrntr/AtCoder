N = int(input())
T = input()

pos = [0, 0]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
x = 0
for i in range(N):
    if T[i] == "S":
        pos[0] += direction[x][0]
        pos[1] += direction[x][1]
    else:
        x += 1
        x %= 4

print(*pos)
