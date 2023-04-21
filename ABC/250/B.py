N, A, B = map(int, input().split())

for i in range(A*N):
    for j in range(B*N):
        if i % (2*A) < A:
            if j % (2*B) < B:
                print('.', end='')
            else:
                print('#', end='')
        else:
            if j % (2*B) < B:
                print('#', end='')
            else:
                print('.', end='')
    print()