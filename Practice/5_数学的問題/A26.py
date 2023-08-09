Q = int(input())

for _ in range(Q):
    x = int(input())
    flag = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")