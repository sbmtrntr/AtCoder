#リストSの要素の組み合わせを全列挙
N = 0
S = []
for b in range(1 << N):
    temp = []
    for i in range(N):
        if b >> i & 1:   
            temp.append(S[i])

# cppのbit全探索
# rep(b, 1 << N) {
#     vector<int> temp;
#     rep(i, N) {
#         if ((b & (1 << i)) == 0)
#               temp.pb(S[i]);
#     }
# }