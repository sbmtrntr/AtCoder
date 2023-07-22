a = input()

if int(a[-1]) <= 2:
    print(a[:-2]+ "-")
elif int(a[-1]) <= 6:
    print(a[:-2])
else:
    print(a[:-2]+ "+")