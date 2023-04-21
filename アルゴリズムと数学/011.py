N = int(input())

def f(n):
    prime_list = [True for _ in range(n+1)]
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2,n+1):
        if prime_list[i]:
            for j in range(2*i, n+1, i):
                prime_list[j] = False

    return prime_list

ans_list = f(N)
for p in range(N+1):
    if ans_list[p]:
        print(p, end=' ')

