S1 = input()
S2 = input()
S3 = input()
S = [0, S1, S2, S3]
T = input()

ans = ""
for i in range(len(T)):
    ans += S[int(T[i])]

print(ans)



