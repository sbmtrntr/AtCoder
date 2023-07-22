N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
ans2 = 0

for i in range(N):
    if A[i] == B[i]:
        ans1 += 1
    else:
        if A[i] in B:
            ans2 += 1

        if B[i] in A:
            ans2 += 1

print(ans1)
print(ans2//2)
