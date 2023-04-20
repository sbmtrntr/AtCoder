N = int(input())
b = bin(N)[2:]
a = []
for i in range(len(b)):
    if b[len(b)-i-1] == '1':
        a.append(2**i)

A = []

for b in range(1 << len(a)):
    temp = 0
    for i in range(len(a)):
        if (b & (1 << i) == 0): temp += a[i]
    A.append(temp)

A.sort()

for x in A:
    print(x)