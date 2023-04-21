N = int(input())

l = 1
cnt = 0
i = "11"

S = int(i)

while S <= N:
    cnt += 1
    l += 1
    i = str(l)*2
    S = int(i)

print(cnt)