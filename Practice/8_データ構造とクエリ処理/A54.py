Q = int(input())
db = dict()

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        db[q[1]] = q[2]
    else:
        print(db[q[1]])