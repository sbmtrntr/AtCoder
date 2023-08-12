N = int(input())
S = list(input())
Q = int(input())
T, X, C = [], [], []
komoji = None
idx = -1

for i in range(Q):
    t, x, c = input().split()
    t, x = map(int, (t, x))
    x -= 1
    T.append(t)
    X.append(x)
    C.append(c)
    if t == 2 or t == 3:
        idx = i

for i in range(idx+1):
    if T[i] == 1:
        S[X[i]] = C[i]

if T[idx] == 2:
    komoji = True
if T[idx] == 3:
    komoji = False
    
if komoji is None:
    S = list("".join(S))
elif komoji:
    S = list("".join(S).lower())
else:
    S = list("".join(S).upper())

for i in range(idx+1, Q):
    S[X[i]] = C[i]

print("".join(S))