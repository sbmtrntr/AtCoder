A, B = map(int, input().split())
ans = 0
while A != B:
    if A > B:
        if A % B == 0:
            ans += A // B - 1
            A = A - B*(A//B-1)
        else:
            ans +=  A // B
            A = A - B*(A//B)
    else:
        if B % A == 0:
            ans += B // A - 1
            B = B - A*(B//A-1)
        else:
            ans +=  B // A
            B = B - A*(B//A)
print(ans)