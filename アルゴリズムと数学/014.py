N = int(input())

ans = []
for i in range(2,int(N**0.5)+1):
    while N % i == 0:
        N /= i
        ans.append(i)

if N >= 2:
    ans.append(int(N))

    
print(*ans)

        