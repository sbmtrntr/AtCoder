N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

x = 0

for arr in factorization(N):
    x += arr[1]

ans = 0
while True:
    if 2** ans >= x:
        print(ans)
        break
    ans += 1

