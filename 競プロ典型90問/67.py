N, K = map(int, input().split())

if N == 0:
    print(0)
    exit()

def tenToNine(arg):
        if arg // 9:
            return tenToNine(arg // 9) + str(arg % 9)
        return str(arg % 9)

for _ in range(K):
    deci = 0
    for i in range(len(str(N))):
        deci += int(str(N)[i])*8**(len(str(N))-1-i)

    nine = list(tenToNine(deci))

    for i in range(len(nine)):
        if nine[i] == "8":
            nine[i] = "5"

    N = int(''.join(nine))

print(''.join(nine))
