T = int(input())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

for _ in range(T):
    N, D, K = map(int, input().split())
    hoge = gcd(D, N)
    if hoge == 1:
        print((K-1)*D%N)
    else:
        if N // hoge >= K:
            print((K-1)*D%N)
        else:
            print((K-1)*D%N+(K-1)//(N//hoge))