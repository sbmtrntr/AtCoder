N = int(input())

num = []

for i in range(1, 2*N+2):
    num.append(i)

while True:
    print(num[0])
    del num[0]
    if num == []:
        break
    x = int(input())
    num.remove(x)
