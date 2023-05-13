N = int(input())
S = input()
t, a = 0, 0
for i in range(N):
    if S[i] == 'T':
        t += 1
    else:
        a += 1

if t > a:
    print('T')
elif a < t:
    print('A')
else:
    ans = a
    a, t = 0, 0
    for i in range(N):
        if S[i] == 'T':
            t += 1
        else:
            a += 1
        if t == ans:
            print('T')
            break
        if a == ans:
            print('A')
            break