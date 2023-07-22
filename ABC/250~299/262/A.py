Y = int(input())

if Y % 4 ==2:
    print(Y)
elif Y % 4 == 1:
    print(Y+1)
elif Y % 4 == 0:
    print(Y+2)
else:
    print(Y+3)