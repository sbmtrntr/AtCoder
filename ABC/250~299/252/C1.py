N = int(input())

S = [input() for _ in range(N)]

ans = 10**9

for i in range(10):
    temp = []
    for s in S:
        for j in range(10):
            num = s[j]
            if num == str(i):
                temp.append(j)

    appeared = []
    temp.sort()
    temp_ans = 0

    for t in temp:
        if t not in appeared:
            x = 0
            temp_ans = max(t, temp_ans)
            appeared.append(t)
        else:
            x += 1
            temp_ans = max(10*x + t, temp_ans)

    ans = min(ans, temp_ans)

print(ans)


