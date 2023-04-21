r, c = map(int, input().split())
A = [[0, 0], [0, 0]]
A[0][0], A[0][1] = map(int, input().split())
A[1][0], A[1][1] = map(int, input().split())

print(A[r-1][c-1])
