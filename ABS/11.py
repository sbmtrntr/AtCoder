N = int(input())

for i in range(N):
    t, x, y = map(int, input().split())
    if (x + y) > t or (x + y) % 2 != (t % 2):
        print("No")
        exit()

print("Yes")