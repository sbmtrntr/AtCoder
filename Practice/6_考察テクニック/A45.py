N, C = input().split()
N = int(N)
A = input()
R, B, W = 0, 0, 0

for i in range(N):
    if A[i] == "R":
        R += 1
    elif A[i] == "B":
        B += 1
    else:
        W += 1

if C == "W":
    if abs(R - B) % 3 == 0:
        print('Yes')
    else:
        print('No')

elif C == 'R':
    if abs(R - B) % 3 == 2:
        print('Yes')
    else:
        print('No')

else:
    if abs(R - B) % 3 == 1:
        print('Yes')
    else:
        print('No')        