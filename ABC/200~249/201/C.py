S = input()

ans = 0

for i in range(10000):
    flag = [False]*10

    for j in range(4):
        flag[i%10] = True #一桁目に使われている数字のとこだけTrue
        i //= 10 #桁を一つずつずらす

    flag2 = True

    for j in range(10):
        if S[j] == 'o' and not flag[j]: #確実に入ってる数字がiに使われてなかったら
            flag2 = False
        if S[j] == 'x' and flag[j]: #確実に入ってない数字がiに使われてたら
            flag2 = False

    ans += flag2

print(ans)
