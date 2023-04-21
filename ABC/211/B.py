S =  []

for i in range(4):
    S.append(input())

if len(set(S)) == 4:
    print("Yes")
else:
    print('No')