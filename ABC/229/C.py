N, W = map(int, input().split())

AB = {}
A = []

for i in range(N):
    temp = tuple((map(int, input().split())))
    if temp[0] not in AB:    
        AB[temp[0]] = temp[1]
        A.append(temp[0])
    else:
        AB[temp[0]] += temp[1]

A_sort = sorted(A, reverse=True)

weight = 0
ans = 0

for i in range(len(A_sort)):
    ans += A_sort[i] * min(W-weight, AB[A_sort[i]])
    weight += min(W-weight, AB[A_sort[i]])
    if weight == W:
        break

print(ans)