M = int(input())
S1 = input()
S2 = input()
S3 = input()
S1 = S1*M
S2 = S2*M
S3 = S3*M
times = [0]*10

for i in range(10):
    if not (str(i) in S1 and str(i) in S2 and str(i) in S3):
        continue
    ok = [False]*3
    time = 0
    while sum(ok) != 3:
        for j in range(M):
            if sum(ok) == 3:
                break
            if not ok[0] and i == int(S1[j]):
                ok[0] = True
                continue
            if not ok[1] and i == int(S2[j]):
                ok[1] = True
                continue
            if not ok[2] and i == int(S3[j]):
                ok[2] = True
                continue

            time += 1

    times[i] = time + 2
print(min(times)) if min(times) != 0 else print(-1)