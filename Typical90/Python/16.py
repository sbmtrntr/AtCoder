N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for i in range(10000):
    for j in range(10000):
        temp = A*i + B*j
        if (N-temp) % C != 0 or temp > N:
            continue
        k = (N-temp)//C
        ans = min(ans, i+j+k)

print(ans)
