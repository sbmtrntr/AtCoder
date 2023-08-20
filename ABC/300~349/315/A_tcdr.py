S = input()
ans = ""
for s in S:
    if s not in ["a", "i", "u", "e", "o"]:
        ans += s
print(ans)