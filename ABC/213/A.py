A, B = map(int, input().split())

A = bin(A)[2:]
B = bin(B)[2:]

A = "0"*(8-len(A)) + A
B = "0"*(8-len(B)) + B
C = ""

for i in range(8):
    if A[i] == B[i]:
        C += "0"
    else:
        C += "1"

print(int(C, 2))
