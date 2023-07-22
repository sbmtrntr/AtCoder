from collections import deque
N, D = map(int, input().split())
X, Y = [0]*N, [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

infected = set([0])
queue = deque([0])

while queue:
    v = queue.popleft()
    for i in range(N):
        if i not in infected and ((X[i] - X[v])**2 + (Y[i] - Y[v])**2)**0.5 <= D:
            queue.append(i)
            infected.add(i)

for i in range(N):
    if i in infected:
        print('Yes')
    else:
        print('No')