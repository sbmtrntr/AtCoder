from collections import defaultdict
S = input()
T = input()
N = len(S)
dic_s = defaultdict(int)
dic_t = defaultdict(int)
for i in range(N):
    dic_s[S[i]] += 1
    dic_t[T[i]] += 1
hoge = ['a', 't', 'c', 'o', 'd', 'e', 'r']
sa = 0
for k, v in dic_s.items():
    if k == '@':
        continue
    if k in hoge:
        if v > dic_t[k]:
            dic_t['@'] -= v - dic_t[k]
            if dic_t['@'] < 0:
                exit(print('No'))
            else:
                dic_t[k] = v
        elif v < dic_t[k]:
            dic_s['@'] -= dic_t[k] - v
            if dic_s['@'] < 0:
                exit(print('No'))
            else:
                dic_s[k] = dic_t[k]
        else:
            continue
    else:
        if k not in dic_t:
            exit(print('No'))
        else:
            if dic_s[k] != dic_t[k]:
                exit(print('No'))

for k, v in dic_t.items():
    if k == '@':
        continue
    if k in hoge:
        if v > dic_s[k]:
            dic_s['@'] -= v - dic_s[k]
            if dic_s['@'] < 0:
                exit(print('No'))
            else:
                dic_s[k] = dic_t[k]
        elif v < dic_s[k]:
            dic_t['@'] -= dic_s[k] - v
            if dic_t['@'] < 0:
                exit(print('No'))
            else:
                dic_t[k] = dic_s[k]
        else:
            continue
    else:
        if k not in dic_s:
            exit(print('No'))
        else:
            if dic_s[k] != dic_t[k]:
                exit(print('No'))

if dic_s['@'] < 0 or dic_t['@'] < 0:
    print('No')
else:
    print('Yes')