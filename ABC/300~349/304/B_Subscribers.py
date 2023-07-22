N = input()
keta = len(N)
if keta <= 3:
    print(N)
else:
    print(N[:3]+'0'*(keta-3))