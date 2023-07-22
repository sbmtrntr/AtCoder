import math
n, k = map(int, input().split())
A = list(map(int, input().split()))

zahyo = []

for i in range(n):
    zahyo.append(list(map(int, input().split())))

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

dis = [10**6]*n

for i in A:
    x1, y1 = zahyo[i-1][0], zahyo[i-1][1]
    for j in range(n):
        x2, y2 = zahyo[j][0], zahyo[j][1]
        temp = distance(x1, y1, x2, y2)
        if dis[j] > temp:
            dis[j] = temp

print(max(dis))