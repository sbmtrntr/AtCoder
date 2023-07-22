N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

row = Q-P+1
column = S-R+1

masu = [["." for _ in range(column)] for _ in range(row)]

for k in range(max(P-A, R-B), min(Q-A, S-B)+1):
    masu[A+k-P][B+k-R] = "#"

for k in range(max(P-A, B-S), min(Q-A,B-R)+1):
    masu[A+k-P][B-k-R] = "#"

for i in range(row):
    for j in range(column):
        print(masu[i][j], end="")
    print()
