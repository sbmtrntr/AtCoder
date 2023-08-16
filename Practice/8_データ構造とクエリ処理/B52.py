from collections import deque
N, X = map(int, input().split())
A = list(input())
que = deque([X-1])
A[X-1] = '@'
while que:
    pos = que.popleft()
    if pos != 0 and A[pos-1] == '.':
        A[pos-1] = '@'
        que.append(pos-1)
    if pos != N-1 and A[pos+1] == '.':
        A[pos+1] = '@'
        que.append(pos+1)

print("".join(A))