A,B,C,D = map(int,input().split())

blue, red = A, 0

for i in range(1, A+1):
    blue += B
    red += C
    if blue <= red*D:
        print(i)
        exit()

print('-1')
    

