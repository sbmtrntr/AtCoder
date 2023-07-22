N = int(input())
S = input()
W = list(map(int, input().split()))

children = []
adults = []

for i in range(len(S)):
    if S[i] == "0":
        children.append(W[i])
    else:
        adults.append(W[i])

if children == [] or adults == []:
    print(len(children) + len(adults))
    exit()

children.sort()
adults.sort()

ans = 0

if children[-1] < adults[0]:
    print(N)
elif children[0] > adults[-1]:
    print(0)
else:
    for x in range(children[0], adults[len(adults)-1]):
        cnt = 0
        for child in children:
            if child < x:
                cnt += 1
            else:
                break
        
        for adult in reversed(adults):
            if adult >= x:
                cnt += 1
            else:
                break

        if ans > cnt:
            break
        else:
            ans = cnt

    print(ans)


