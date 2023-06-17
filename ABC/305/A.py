N = int(input())
if N % 5 == 0:
    print(N)
elif N % 5 <= 2:
    print(N - N % 5)
else:
    print(N + (5 - N % 5))