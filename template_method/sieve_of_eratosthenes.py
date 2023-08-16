def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime