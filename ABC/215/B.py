N = int(input())

k = 1
while True:
    if 2**k > N:
        print(k-1)
        break
    else:
        k += 1