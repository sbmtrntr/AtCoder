N = int(input())
S = list(input())
Q = int(input())

flip = False

for i in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if flip:
            S[A-N], S[B-N] = S[B-N], S[A-N]
        else:
            S[A], S[B] = S[B], S[A]
    else:
        if flip:
            flip = False
        else:
            flip = True
        
if flip:
    S = S[N:] + S[:N]
    print("".join(S))
else:
    print("".join(S))