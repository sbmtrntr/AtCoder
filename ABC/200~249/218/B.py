P = map(int, input().split())
ans = []
for i in P:
    ans.append(chr(i+96))

print("".join(ans))