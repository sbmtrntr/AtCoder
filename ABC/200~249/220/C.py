N = int(input())
A = list(map(int, input().split()))
x = int(input())

y = sum(A)

i = x//y

z = y*i
cnt = 0
while True:
    if z > x:
        print(len(A)*i + cnt)
        break
    else:
        z += A[cnt]
        cnt += 1