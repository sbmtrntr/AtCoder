N = int(input())
ans = [[0, 0]]

for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        ans.append([ans[-1][0]+p, ans[-1][1]])
    else:
        ans.append([ans[-1][0], ans[-1][1] + p])

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    
    print(ans[R][0]- ans[L-1][0], ans[R][1]- ans[L-1][1])
