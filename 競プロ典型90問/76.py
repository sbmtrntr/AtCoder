N = int(input())
A = list(map(int, input().split()))

B = [0]

for a in A:
    B.append(B[-1] + a)

x = B[-1]

if x % 10 != 0:
    print('No')
    exit()

B = set(B)

for b in B:
    if (b + x // 10) % x in B:
        print('Yes')
        exit()

print('No')