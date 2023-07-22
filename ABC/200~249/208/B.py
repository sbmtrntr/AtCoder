import math

P = int(input())

a = []

for i in range(1, 11):
    a.append(math.factorial(i))

ans = 1
flag = True

while flag:
    for j in range(10):
        if P < a[j]:
            P -= a[j-1]
            break
        elif P == a[j]:
            print(ans)
            flag = False
            break
        elif j == 9 and P > a[9]:
            P -= a[9]
    ans += 1
