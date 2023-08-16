from bisect import bisect_left, bisect_right, insort
Q = int(input())
table = []

for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        insort(table, x)
    else:
        if len(table) == 0:
            print(-1)
        else:
            idx = bisect_left(table, x)
            if idx < len(table):
                print(min(abs(x - table[idx-1]), abs(x - table[idx])))
            else:
                print(abs(x-table[idx-1]))