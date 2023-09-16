import math
M  = int(input())
S1 = input()
S2 = input()
S3 = input()
ans = 10**9
for i in range(3*M):
    for j in range(3*M):
        for k in range(3*M):
            if i != j and j != k and i != k and S1[i%M] == S2[j%M] and S2[j%M] == S3[k%M]:
                ans = min(ans, max(i, j, k))

print(ans) if ans != 10**9 else print(-1)