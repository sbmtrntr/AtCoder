x = list(input())
N = int(input())

dic = {}

for i in range(26):
    dic[x[i]] = str(11+i)

ans_dic = {}

for i in range(N):
    s = input()
    new_s = s
    if len(s) < 10:
        new_s += "0"*(10-len(s))
    num_s = ""
    for j in range(10):
        if new_s[j] == "0":
            num_s += "10"
        else:
            num_s += dic[s[j]]
    ans_dic[int(num_s)] = s

ans = sorted(ans_dic.items())

for i in ans:
    print(i[1])

