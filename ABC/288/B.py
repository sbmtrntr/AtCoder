N, K = map(int, input().split())
S = [input() for _ in range(N)]
T = []
for i in range(K):
    T.append(S[i])

T.sort()
for i in range(K):
    print(T[i])