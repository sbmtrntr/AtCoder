N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(i+j)