N, X = map(int, input().split())
A =list(map(int, input().split()))

friend_list = [False]*N

while not friend_list[X-1]:
    friend_list[X-1] = True
    X = A[X-1]
    
print(sum(friend_list))
