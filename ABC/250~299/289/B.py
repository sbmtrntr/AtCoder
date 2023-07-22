N, M = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
ans = []
stack = []
idx = 0
for i in range(1, N+1):
    next = a[idx]
    if i != next:
        ans.append(i)
        if len(stack) != 0:
            for j in range(len(stack)):
                ans.append(stack[len(stack) - j - 1])
        stack.clear()
    else:
        stack.append(i)
        idx += 1

print(*ans)