N, Q = map(int, input().split())

S = input()

ind = 0
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        ind += x
    else:
        print(S[(x-ind-1)%N])



