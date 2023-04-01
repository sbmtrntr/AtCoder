S = input()

if not S[0].isupper():
    exit(print("No"))

try:
    a = int(S[1:7])
except:
    exit(print('No'))

if 100000 <= int(S[1:7]) < 1000000:
    pass
else:
    exit(print('No'))

if S[-1].isupper():
    print('Yes')
else:
    print('No')