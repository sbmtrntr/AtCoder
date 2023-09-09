N = int(input())
s = ""

for i in range(N+1):
    flag = True
    for j in range(1, 10):
        if N % j == 0 and i % (N // j)== 0:
            s += str(j)
            flag = False
            break
    
    if flag: s += '-'

print(s)