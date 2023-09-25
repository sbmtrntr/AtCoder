N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(101):
    temp = sorted(A + [i])
    if sum(temp) - min(temp) - max(temp) >= X:
        exit(print(i))
    

print(-1)