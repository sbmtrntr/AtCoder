N = int(input())

a = list(map(int, input().split()))

a.sort()
ans = 0
x = 0
for i in reversed(a):
    if x % 2 == 0: ans += i
    else: ans -= i
    x += 1

print(ans)
