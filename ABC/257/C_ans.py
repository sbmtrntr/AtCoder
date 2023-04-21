N = int(input())
S = input()
W = list(map(int, input().split()))

pair = []

for i in range(N):
    if S[i] == "1":
        pair.append([W[i], "0"])
    else:
        pair.append([W[i], "1"])

pair.sort()

ans = 0

for i in range(len(S)):
    if S[i] == "1":
        ans += 1

max_ans = ans

for i in range(N):
    if pair[i][1] == '0':
        ans -= 1
    else:
        ans += 1

    max_ans = max(max_ans, ans)

print(max_ans)