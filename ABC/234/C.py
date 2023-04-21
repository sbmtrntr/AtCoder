K = int(input())

x = []

while True:
    x.append(K%2)
    K //= 2

    if K == 0:
        break

ans = ""
for i in range(len(x)-1, -1, -1):
    if x[i] == 1:
        ans += "2"
    else:
        ans += "0"

print(ans)