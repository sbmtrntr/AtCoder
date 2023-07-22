x = input()

if int(x[-3]) < 5:
    print(int(x[:-4]))
else:
    print(int(x[:-4])+1)
