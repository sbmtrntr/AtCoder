from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))
elements = set()
queue = deque([])
ans = 0
temp = 0

for i in range(N):
    if N[i] in elements:
        temp += 1
    else:
        if len(elements) < K:
            temp += 1
            elements.add()
            queue.append(N[i])
        else:
            queue.popleft()
            ans = max(ans, temp)
            temp = 0

print(ans)