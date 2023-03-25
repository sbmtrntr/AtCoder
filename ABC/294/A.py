<<<<<<< HEAD
N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] % 2 == 0:
        ans.append(A[i])

=======
N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] % 2 == 0:
        ans.append(A[i])

>>>>>>> bafeeda5f8b5c60ae86c2edaeeb88702f25eca53
print(*ans)