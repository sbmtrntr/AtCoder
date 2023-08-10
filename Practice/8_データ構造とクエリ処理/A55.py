from bisect import bisect_left, insort_left

Q = int(input())

s = []
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        insort_left(s, q[1])
    elif q[0] == 2:
        idx = bisect_left(s, q[1])
        s.pop(idx)
    else:
        idx = bisect_left(s, q[1])
        if idx < len(s):
            print(s[idx])
        else:
            print(-1)
