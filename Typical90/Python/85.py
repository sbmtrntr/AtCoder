K = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisors = make_divisors(K)
c_kouho = set(divisors)
N = len(divisors)
ans = 0

for i in range(N):
    for j in range(i, N):
        c = K / (divisors[i]*divisors[j])
        if c.is_integer() and int(c) in c_kouho and c >= divisors[j]:
            ans += 1

print(ans)