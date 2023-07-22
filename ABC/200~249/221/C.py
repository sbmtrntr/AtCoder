n = input()
ans = 0

for bitnum in range(1<<len(n)):
    a = []
    b = []
    for i in range(len(n)):
        if (bitnum >> i) & 1 == 0:
            a.append(n[i])
        else:
            b.append(n[i])
    
    if a == [] or b == []:
        continue
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_join="".join(a)
    b_join="".join(b)
    tmp_ans=int(a_join)*int(b_join)
    ans=max(ans,tmp_ans)

print(ans)


# import itertools

# N = list(map(int, input()))

# ans = 0

# for i in range(1, len(N)):
#     for x in itertools.permutations(N, i):
#         copyN = N.copy()
#         for y in x:
#             copyN.remove(y)
#         z_str = ""
#         for z in x:
#             z_str += str(z)
#         n_str = ""
#         for n in copyN:
#             n_str += str(n)
#         mul = int(z_str) * int(n_str)
#         print(z_str, n_str)
#         ans = max(ans, mul)

# print(ans)


