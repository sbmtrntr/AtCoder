M = int(input())
D = list(map(int, input().split()))
mid = (sum(D) + 1) // 2
acc = 0
for i in range(M):
    acc += D[i]
    if acc >= mid:
        exit(print(i+1, D[i]-(acc-mid)))