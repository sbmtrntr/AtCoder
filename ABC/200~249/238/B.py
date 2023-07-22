n = int(input())
a = list(map(int, input().split()))


arg = 0
kirekomi = []
kirekomi.append(0)
kirekomi.append(360)
for i in range(n):
    arg += a[i]
    if arg <= 359:
        kirekomi.append(arg)
    else:
        arg = arg % 360
        kirekomi.append(arg)

mx = 0
kirekomi.sort()
for i in range(n+1):
    mx = max(mx, kirekomi[i+1] - kirekomi[i])

print(mx)