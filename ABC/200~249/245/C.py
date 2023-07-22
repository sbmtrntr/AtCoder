N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp_a = [False]*N
dp_b = [False]*N

dp_a[0] = True
dp_b[0] = True

for i in range(1, N):
    if dp_a[i-1]:
        if abs(A[i-1] - A[i]) <= K:
            dp_a[i] = True
        if abs(A[i-1] - B[i]) <= K:
            dp_b[i] = True

    if dp_b[i-1]:
        if abs(B[i-1] - A[i]) <= K:
            dp_a[i] = True
        if abs(B[i-1] - B[i]) <= K:
            dp_b[i] = True


if dp_a[-1] or dp_b[-1]:
    print('Yes')
else:
    print('No')