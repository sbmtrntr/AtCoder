K = int(input())

if K < 60:
    H = "21"
else:
    H = "22"


M = str(K % 60)

if len(M) == 1:
    M = "0" + M
print(H+":"+M)
