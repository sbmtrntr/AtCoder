import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(q):
    x = int(input())
    ind = bisect.bisect(A, x)
    
    if A[ind-1] != x:
        print(n-ind)
    else:
        print(n-ind+1)
        
