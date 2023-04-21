n = int(input())
a = list(map(int, input().split()))

cnt = 0
k_cnt = 0
pre_k = 0
for i in range(n):
    k = a[i]
    k_cnt += 1
    if pre_k == k:
        if k_cnt == k:
            cnt -= k
    else:
        k_cnt = 0
    cnt += 1
    print(cnt)
    pre_k = k
