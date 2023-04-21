N, Y = map(int, input().split())

Y /= 1000

for z in range(N+1):
    if z > Y: break
    for y in range(N+1):
        if 5 * y > Y: break
        x = N - z - y
        if x >= 0 and 10*x + 5*y + z == Y:
            print(x, y, z)
            exit()

print("-1 -1 -1")
