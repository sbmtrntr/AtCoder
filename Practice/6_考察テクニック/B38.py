N = int(input())
S = "X" + input()
height = [0]*N
height[0] = 1

for i in range(1, N):
    for j in range(1, N):
        if S[i] == 'A':
            height[i] = height[i-1] + 1
        else:
            height[i] = height[i-1] - 1

