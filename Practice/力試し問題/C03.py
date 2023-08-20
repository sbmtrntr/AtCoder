D = int(input())
X = int(input())
A = [0]*D
A[0] = X
for i in range(1, D):
    a = int(input())
    A[i] = A[i-1] + a
Q = int(input())

for _ in range(Q):
    s, t = map(int, input().split())
    if A[s-1] > A[t-1]:
        print(s)
    elif A[s-1] == A[t-1]:
        print('Same')
    else:
        print(t)