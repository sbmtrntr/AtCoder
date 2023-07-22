import heapq
from collections import defaultdict

Q = int(input())

mx = []
mn = []
S = defaultdict(int)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        S[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)

    elif query[0] == 2:
        x, c = query[1:]
        S[x] = max(0, S[x] - c)

    else:
        while S[-mx[0]] == 0:
            heapq.heappop(mx)
        while S[mn[0]] == 0:
            heapq.heappop(mn)
        print(-mx[0] - mn[0])    
        