N, Q = map(int, input().split())
not_called = [i for i in range(1, N+1)]
called = set()
ans = 1
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        calling = not_called.pop(0)
        called.add(calling)
    elif q[0] == 2:
        called.remove(q[1])
        if ans not in called:
            ans = min(called)
    else:
        print(ans)