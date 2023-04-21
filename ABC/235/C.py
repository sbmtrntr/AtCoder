N, Q = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    if A[i] not in dic:
        dic[A[i]] = [i+1]
    else:
        dic[A[i]].append(i+1)

for i in range(Q):
    x, k = map(int, input().split())
    try:
        if k <= len(dic[x]):
            print(dic[x][k-1])
        else:
            print(-1)
    
    except:
        print(-1)
    
    
