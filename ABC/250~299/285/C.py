N = int(input())
S = input()
ans = 0

for i in range(1, N):
    ans = 0
    for k in range(1, N-i+1):
        if S[k-1] != S[k+i-1]:
            ans = k
        else:
            break
    print(ans)