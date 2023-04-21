N = int(input())
A = list(map(int, input().split()))
ans = N*sum(x**2 for x in A)
ans -= sum(x for x in A) ** 2
print(ans)
