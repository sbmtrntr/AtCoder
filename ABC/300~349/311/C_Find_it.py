N = int(input())
A = list(map(int, input().split()))
graph = {}
for i in range(N):
    graph[i+1] = A[i]

for i in range(1, N+1):
    nxt = i
    seen = set()
    junban = []
    while True:
        if nxt in seen:
            ans1 = 0
            ans2 = []
            flag = False
            for a in junban:
                if flag:
                    ans1 += 1
                    ans2.append(a)
                if a == nxt:
                    flag = True
                    ans1 += 1
                    ans2.append(a)
            print(ans1)
            print(*ans2)
            exit()
        seen.add(nxt)
        junban.append(nxt)
        nxt = graph[nxt]
        