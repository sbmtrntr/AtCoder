N = int(input())

S = [0]*N

for i in range(N):
    if i == 0:
        S[0] = [1]
        continue
    S[i] = S[i-1] + [i+1] + S[i-1]

print(*S[-1])