x1, y1, x2, y2 = map(int, input().split())

x_list = [[x1+1, y1+2], [x1+2, y1+1], [x1-1, y1-2], [x1-2, y1-1], [x1+1, y1-2], [x1+2, y1-1], [x1-1, y1+2], [x1-2, y1+1]]
y_list = [[x2+1, y2+2], [x2+2, y2+1], [x2-1, y2-2], [x2-2, y2-1], [x2+1, y2-2], [x2+2, y2-1], [x2-1, y2+2], [x2-2, y2+1]]

for x in x_list:
    if x in y_list:
        print("Yes")
        exit()

print("No")

