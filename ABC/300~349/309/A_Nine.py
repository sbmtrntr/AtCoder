A, B = map(int, input().split())
if (A == 3 and B == 4) or (A == 6 and B == 7) or B - A != 1:
    print('No')
else:
    print('Yes')