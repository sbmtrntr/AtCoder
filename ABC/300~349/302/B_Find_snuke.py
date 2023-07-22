H, W = map(int, input().split())
S = [input() for _ in range(H)]
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(H):
    for j in range(W):
        for k in range(8):
            temp = ""
            for l in range(5):
                x = i+l*dir[k][0]
                y = j+l*dir[k][1]
                if x < 0 or x >= H or y < 0 or y >= W:
                    break
                temp += S[x][y]
            if temp == "snuke":
                for l in range(5):
                    x = i+l*dir[k][0]
                    y = j+l*dir[k][1]
                    print(x+1, y+1)