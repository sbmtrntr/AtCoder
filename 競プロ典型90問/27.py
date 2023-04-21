from collections import defaultdict
d = defaultdict(int)

N = int(input())

for i in range(N):
    S = input()
    if not d[S]:
        d[S] = 1
        print(i+1)
