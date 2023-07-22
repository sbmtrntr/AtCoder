S = [input() for _ in range(8)]
row = "abcdefgh"
column = "87654321"
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            exit(print(row[j]+column[i]))