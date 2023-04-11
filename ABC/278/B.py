H, M = input().split()

while True:
    if len(H) == 1:
        H = '0' + H
    if len(M) == 1:
        M = '0' + M

    h = int(H[0] + M[0])
    m = int(H[1] + M[1])

    if 0 <= h <= 23 and 0 <= m <= 59:
        print(H, M)
        break

    M = str((int(M) + 1) % 60)
    if (int(M) % 60 == 0): H = str((int(H) + 1) % 24)
