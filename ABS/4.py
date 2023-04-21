N = int(input())
A = list(map(int, input().split()))

cnt = 0

def ok(A):
    for x in A:
        if x % 2 == 1:
            return False

    return True

while ok(A):
    cnt += 1
    for i in range(len(A)):
        A[i] /= 2

print(cnt)
    