N = int(input())
hoge = []
for i in range(N):
    s, a = input().split()
    hoge.append([s, int(a)])
mn_idx = -1
mn = 10**9+1
for i in range(N):
    if mn > hoge[i][1]:
        mn = hoge[i][1]
        mn_idx = i

for i in range(N):
    print(hoge[(i+mn_idx)%N][0])