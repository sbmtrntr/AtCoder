N = int(input())
S = list(input())
Q = int(input())

flip = False

for i in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flip:
            S[a-N], S[b-N] = S[b-N], S[a-N]
        else:
            S[a], S[b] = S[b], S[a]
    else:
        if flip:
            flip = False
        else:
            flip = True

if flip:
    S = S[N:] + S[:N]

print("".join(S))