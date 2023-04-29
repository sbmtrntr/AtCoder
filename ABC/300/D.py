import math

# エラトステネスの篩
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

N = int(input())
# M以下の整数の素数判定
prime = prime(3*10**5)

# 素数判定を基に, 素数リストを作成
prime_list = []
for i in range(3*10**5):
    if prime[i]:
        prime_list.append(i)

ans = 0

for i in range(len(prime_list)):
    k = len(prime_list) - 1
    j = i+1
    while j < k:
        num = prime_list[i]**2 * prime_list[j] * prime_list[k]**2
        if num > N:
            k -= 1

print(ans)