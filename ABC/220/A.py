A, B, C = map(int, input().split())

for i in range(1, B//C+1):
    if A <= C*i <= B:
        print(C*i)
        exit()

print(-1)