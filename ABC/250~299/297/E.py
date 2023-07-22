N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = set()
for b in range(1, 1 << N):
    temp = 0
    for i in range(N):
        if b >> i & 1:   
            temp += A[i]
    ans.add(temp)