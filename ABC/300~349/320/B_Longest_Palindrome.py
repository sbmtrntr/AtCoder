S = input()
ans = 0

def check(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True

for i in range(len(S)):
    for j in range(len(S)):
        temp = S[i:j+1]
        if check(temp):
            ans = max(ans, len(temp))

print(ans)