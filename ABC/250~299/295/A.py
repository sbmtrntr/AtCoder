N = int(input())
W = list(input().split())
for i in range(N):
    if W[i] in ['and', 'not', 'that', 'the', 'you']:
        exit(print('Yes'))
print('No')
        