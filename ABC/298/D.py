from collections import deque
Q = int(input())
mod = 998244353
p10 = [0]*6*10**5
p10[0] = 1
for i in range(1, 6*10**5):
    p10[i] = p10[i-1]*10 % mod

deq = deque()
deq.append(1)
ans = 1
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        deq.append(q[1])
        ans = (ans*10 + q[1]) % mod
    elif q[0] == 2:
        ans -= (p10[len(deq)-1]*deq[0]) % mod
        deq.popleft()
    else:
        print(ans % mod)