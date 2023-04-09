N = int(input())
S = input()
prev = S[0]
for i in range(1, len(S)):
    if S[i] == prev:
        exit(print("No"))
    prev = S[i]
print("Yes")