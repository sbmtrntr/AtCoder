N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ok = [False] * N

C = []
for i in range(N):
    C.append(A[i] + B[i])

math_dic = {}
eng_dic = {}
dic = {}
A_sort = sorted(A, reverse=True)
B_sort = sorted(B, reverse=True)
C_sort = sorted(C, reverse=True)


for i in range(N):
    math_dic[i+1] = A[i]
    eng_dic[i+1] = B[i]
    dic[i+1] = C[i]

ok = []

for i in range(X):
    for k, v in math_dic.items():
        if A_sort[i] == v:
            ok.append(k)
            X -= 1
        if X == 0:
            break
            
for i in ok:
    del eng_dic[i]
    del dic[i]

print(math_dic)
print(eng_dic)
print(ok)

for i in range(Y):
    for k, v in eng_dic.items():
        if B_sort[i] == v:
            ok.append(k)
            Y -= 1
        if Y == 0:
            break

for i in ok:
    try:
        del dic[i]
    except:
        continue

print(math_dic)
print(eng_dic)
print(ok)

for i in range(Z):
    for k, v in dic.items():
        if C_sort[i] == v:
            ok.append(k)
            Z -= 1
        if Z == 0:
            break

print(math_dic)
print(eng_dic)
print(ok)

ok.sort()

for a in ok:
    print(a)




