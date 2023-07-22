S = list(input())
length = len(set(S))
if length == 3:
    print(6)
elif length == 2:
    print(3)
else:
    print(1)