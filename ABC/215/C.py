S, K = input().split()

from itertools import permutations

st = set()
for it in permutations(S):
    st.add("".join(it))

print(sorted(st)[int(K)-1])
