N, K = map(int,input().split())
# 2-2, 3-4, 4-6, 5-8
if K % 2 == 0 and (N-1)*2 <= K:
    print('Yes')
else:
    print('No')