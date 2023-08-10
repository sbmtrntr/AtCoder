import heapq
Q = int(input())
p_queue = []
heapq.heapify(p_queue)

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        heapq.heappush(p_queue, q[1])
    elif q[0] == 2:
        print(p_queue[0])
    else:
        heapq.heappop(p_queue)