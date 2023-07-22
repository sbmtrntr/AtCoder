S = input()
x, y = -1, -1
for i in range(8):
    if x == -1 and S[i] == 'B':
        x = i
    elif S[i] == 'B':
        y = i
if  (x + y) % 2 == 0:
    exit(print('No'))

x, y, z = -1, -1, -1

for i in range(8):
    if x == -1 and S[i] == 'R':
        x = i
    elif S[i] == 'R':
        y = i
    if S[i] == 'K':
        z = i

if x < z < y:
    print('Yes')
else:
    print('No')