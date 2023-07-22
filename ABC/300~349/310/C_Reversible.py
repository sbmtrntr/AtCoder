N = int(input())
S = set()
for _ in range(N):
    s = input()
    if s not in S and s[::-1] not in S:
        S.add(s)
print(len(S))