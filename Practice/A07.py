D = int(input())
N = int(input())

accum = [0]*(D+2)

for i in range(N):
    L, R = map(int, input().split())
    accum[L] += 1
    accum[R+1] -= 1

for i in range(D):
    accum[i+1] += accum[i]

print(*accum[1:-1])