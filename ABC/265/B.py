N, M, T = map(int, input().split())
A = list(map(int, input().split()))

dic = {}

for i in range(M):
    x, y = map(int, input().split())
    dic[x] = y

now = 1

while now < N:
    if now in dic:
        T += dic[now]
    T -= A[now-1]
    now += 1
    if T <= 0:
        print("No")
        exit()

print("Yes")