N, X = map(int, input().split())

S = ""
for i in range(26):
    S += chr(65+i)*N

print(S[X-1])