N = int(input())

def judge(S):
    x = 0
    for i in range(len(S)):
        if S[i] == '(':
            x += 1
        else:
            x -= 1
        if x < 0:
            return False
    if x == 0:
        return True
    return False

for b in range(1 << N):
    S = ""
    for i in range(N):
        if (b & (1 << i)) == 0:
            S = "(" + S
        else:
            S = ")" + S

    if judge(S): print(S)
