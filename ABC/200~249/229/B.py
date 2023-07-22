A, B =  input().split()

if len(A) < len(B):
    for i in range(len(A)):
        if int(A[len(A)- i - 1]) + int(B[len(B)- i - 1]) > 9:
            print('Hard')
            exit()
else:
    for i in range(len(B)):
        if int(A[len(A)- i - 1]) + int(B[len(B)- i - 1]) > 9:
            print('Hard')
            exit()

print('Easy')
