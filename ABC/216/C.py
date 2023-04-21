N = int(input())

ans = ""

for i in range(120):
    if N % 2 == 0 and N != 0:
        N //= 2
        ans = "B" + ans
    else:
        N -= 1
        ans = "A" + ans
    if N == 0:
        break

print(ans)


