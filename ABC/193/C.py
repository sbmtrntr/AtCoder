N = int(input())

ans = N
dic = {}

for a in range(2, 10**5):
    for b in range(2, 101):
        num = a**b
        if num <= N and num not in dic:
            ans -= 1
            dic[num] = 1
        else:
            break

print(ans)