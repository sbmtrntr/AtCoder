T = int(input())

A=list(range(2,3*10**6+1))
p=list()
while A[0]**2<=3*10**6:
	tmp=A[0]
	p.append(tmp)
	A=[e for e in A if e%tmp!=0]
primes = p + A

for _ in range(T):
    N = int(input())
    for p in primes:
        if N % p**2 == 0:
            print(p, N // p**2)
            break
        if N % p == 0:
            print(int((N // p)**0.5), p)
            break