h1, h2, h3, w1, w2, w3 = map(int, input().split())

h = [h1, h2, h3]
w = [w1, w2, w3]

column = [0, 0, 0]

column_kouho = [[], [], []]
for n in range(3):
    for i in range(1, h[n]+1):
        column[0] = i
        for j in range(1, h[n]+1):
            column[1] = j
            for k in range(1, h[n]+1):
                column[2] = k
                if sum(column) > h[n]:
                    break
                elif sum(column) == h[n]:
                    column_kouho[n].append(column.copy())

ans = 0
row = [0, 0, 0]
row_kouho = [[], [], []]
for x in range(3):
    for i in range(len(column_kouho[0])):
        row[0] = column_kouho[0][i][x]
        for j in range(len(column_kouho[1])):
            row[1] = column_kouho[1][j][x]
            for k in range(len(column_kouho[2])):
                row[2] = column_kouho[2][k][x]
                if sum(row) > w[x]:
                    break
                elif sum(row) == w[x]:
                    row_kouho[x].append(row.copy())
                                    

print(row_kouho)




        
