N = int(input())

money = 0
day = 1
while True:
    money += day
    if N <= money:
        print(day)
        break
    day += 1