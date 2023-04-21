S = input()

S = S[::-1]

S = S.replace("maerd", "").replace("esare", "").replace("resare", "").replace("remaerd", "")

if len(S) == 0: print("YES")
else: print("NO")