N, X, Y = map(int, input().split())
P, T = [], []
for _ in range(N-1):
    p, t = map(int, input().split())
    P.append(p)
    T.append(t)

Q = int(input())

memo = [0]*840
for i in range(8):
    for j in range(N):
        memo

for _ in range(Q):
    q = int(input())
    print(X + q + memo[(X + q) % 8] + Y)