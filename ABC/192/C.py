N, K = map(int, input().split())

a = [0]*(K+1)
a[0] = N

def g1(x):
    temp = list(str(x))
    temp.sort(reverse=True)
    return int("".join(temp))

def g2(x):
    temp = list(str(x))
    temp.sort()
    return int("".join(temp))

def f(x):
    return g1(x) - g2(x)
for i in range(1, K+1):
    a[i] = f(a[i-1])

print(a[-1])
