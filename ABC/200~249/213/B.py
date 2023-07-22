N = int(input())

A = list(map(int, input().split()))
dic = {}

for i in range(N):
    dic[A[i]] = i+1

A.sort()

print(dic[A[N-2]])

