N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):
    now = H[i]
    if i+1 == N-1 and H[i] < H[i+1]:
        now = H[i+1]

    if H[i] >= H[i+1]:
        break
    

print(now)
    