N = input()

ans = 0
for i in range(1, len(N)):
    ans += (i-1) // 3 * (10**i - 10**(i-1))

ans += (int(N) - 10**(len(N)-1) + 1) * ((len(N) - 1) // 3)

print(ans)