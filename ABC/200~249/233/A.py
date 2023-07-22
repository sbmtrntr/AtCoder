x, y = map(int, input().split())

money = x
ans = 0

while money < y:
    money += 10
    ans += 1

print(ans)