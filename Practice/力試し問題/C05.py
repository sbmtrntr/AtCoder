N = int(input())
ans = bin(N-1)[2:]
ans = "0"*(10 - len(ans)) + ans
ans = list(ans)
for i in range(10):
    if ans[i] == "0":
        ans[i] = "4"
    else:
        ans[i] = "7"

print("".join(ans))