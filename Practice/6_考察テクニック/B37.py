N = int(input())
ans = [0]*10

# 1の位が1になるとき
# if N % 10 == 0:
#     ans += N // 10
# else:
#     ans += N // 10 + 1

# 1の位がiになるとき
# for i in range(1, 10):
#     if N % 10 <= i-1:
#         ans[i] += N // 10
#     else:
#         ans[i] += N // 10 + 1

# iの位がjになるとき
for i in range(1, len(str(N))+1):
    for j in range(1, 10):
        if N % 10**i < j-1:
            ans[j] += N // 10**i
        else:
            ans[j] += N // 10**i + 1

print(ans)