M = int(input())
S = []
for i in range(3):
	S.append(input())
ans = 10**9

cnt=[[0 for j in range(M)]for i in range(10)]
for i in range(3):
	for j in range(M):
		cnt[int(S[i][j])][j]= cnt[int(S[i][j])][j]+1

print(cnt)
mx=[0 for i in range(10)]
for i in range(10):
	for j in range(M):
		mx[i]=max(mx[i], M * (cnt[i][j] - 1) + j)

print(mx)
ans = min(mx)

print(ans) if ans != 0 else print(-1)