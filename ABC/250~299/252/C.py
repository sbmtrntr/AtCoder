n=int(input())
s=[]
for i in range(n):
	s.append(input())

cnt=[[0 for j in range(10)]for i in range(10)]
for i in range(n):
	for j in range(10):
		cnt[int(s[i][j])][j]= cnt[int(s[i][j])][j]+1

mx=[0 for i in range(10)]
for i in range(10):
	for j in range(10):
		mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)

print(mx)
print(min(mx))

""" N = int(input())

S = []
for i in range(N):
    S.append(input())

flag =False
X = [0]*10

for i in range(10):
    for j in range(N):
        X[int(S[j][i])] += 1
        if max(X) == N:
            num = X.index(max(X))
            flag = True
            break
    if flag: break

Y = [0]*N
for i in range(N):
    for j in range(10):
        if int(S[i][j]) == num:
            Y[i] = j

if len(Y) == len(set(Y)):
    print(max(Y))
else:
    Z = [0]*N
    for i in range(N):
        Z[Y[i]] += 1
    print((max(Z)-1)*10 + Z.index(max(Z)))

 """