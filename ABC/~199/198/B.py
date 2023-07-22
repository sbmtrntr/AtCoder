N = input()

flag = False

for i in range(10):
    x = "0"*i + N
    rev_x = ""
    for j in range(len(x)):
        rev_x += x[len(x)-j-1]
    
    if x == rev_x:
        flag = True

if flag:
    print("Yes")
else:
    print("No")

