N = int(input())
S = list(input())

pality = 0
for i in range(N):
    if pality % 2 == 0:
        if S[i] == ',':
            S[i] = '.'
    if S[i] == "\"":
        pality += 1

print("".join(S))
