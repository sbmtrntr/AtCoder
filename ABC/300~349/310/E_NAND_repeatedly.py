N = int(input())
S = input()
# n番目の文字に対して、0で回ってきたときと1で回ってきたときの総和を保持
accum = [[0, 0] for _ in range(N+1)]
for i in range(1, N):
    if S[i] == '0':
        accum[i+1][0] = accum[i][0] + 1
        accum[i+1][0] = accum[i][1] + 1
    else:
        accum[i+1][1] = accum[i][0] + 1
        accum[i+1][1] = accum[i][1]

print(accum)