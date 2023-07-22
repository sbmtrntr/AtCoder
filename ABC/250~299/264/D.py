S = list(input())
ans = 0

for i in range(7):
    if S[i] == "a":
        ans += abs(0-i)
    elif S[i] == "t":
        ans += abs(1-i)
    elif S[i] == "c":
        ans += abs(2-i)
    elif S[i] == "o":
        ans += abs(3-i)
    elif S[i] == "d":
        ans += abs(4-i)
    elif S[i] == "e":
        ans += abs(5-i)
    elif S[i] == "t":
        ans += abs(6-i)

print(ans)