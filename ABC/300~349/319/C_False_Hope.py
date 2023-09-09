# masu = []

# for i in range(3):
#     masu.append(list(map(int, input().split())))
# cnt = 0
# # 横
# for i in range(3):
#     seen = set()
#     for j in range(3):
#         seen.add(masu[i][j])
#     if len(seen) == 2:
#         cnt += 1

# # 縦
# for i in range(3):
#     seen = set()
#     for j in range(3):
#         seen.add(masu[j][i])
#     if len(seen) == 2:
#         cnt += 1

# # 斜め
# seen = set()
# seen.add(masu[0][0])
# seen.add(masu[1][1])
# seen.add(masu[2][2])
# if len(seen) == 2:
#     cnt += 1

# seen = set()
# seen.add(masu[0][2])
# seen.add(masu[1][1])
# seen.add(masu[2][0])
# if len(seen) == 2:
#     cnt += 1

# print('{:.8f}'.format(1.0 - cnt/3))

from itertools import permutations
masu = []

for i in range(3):
    masu.append(list(map(int, input().split())))

cnt = 0

for per in permutations(range(9)):
    temp = [[0]*3 for _ in range(3)]
    flag = False
    for num in per:
        if num == 0:
            if temp[0][1] == temp[0][2] and temp[0][1] != 0:
                flag = True
                break
            if temp[1][0] == temp[2][0] and temp[1][0] != 0:
                flag = True
                break
            if temp[1][1] == temp[2][2] and temp[1][1] != 0:
                flag = True
                break
            temp[0][0] = masu[0][0]
        elif num == 1:
            if temp[0][0] == temp[0][2] and temp[0][0] != 0:
                flag = True
                break
            if temp[1][1] == temp[2][1] and temp[1][1] != 0:
                flag = True
                break
            temp[0][1] = masu[0][1]
        elif num == 2:
            if temp[0][1] == temp[0][0] and temp[0][1] != 0:
                flag = True
                break
            if temp[1][2] == temp[2][2] and temp[1][2] != 0:
                flag = True
                break
            if temp[1][1] == temp[2][0] and temp[1][1] != 0:
                flag = True
                break
            temp[0][2] = masu[0][2]
        elif num == 3:
            if temp[0][0] == temp[2][0] and temp[0][0] != 0:
                flag = True
                break
            if temp[1][1] == temp[1][2] and temp[1][1] != 0:
                flag = True
                break
            temp[1][0] = masu[1][0]
        elif num == 4:
            if temp[1][0] == temp[1][2] and temp[1][0] != 0:
                flag = True
                break
            if temp[0][1] == temp[2][1] and temp[0][1] != 0:
                flag = True
                break
            if temp[0][0] == temp[2][2] and temp[0][0] != 0:
                flag = True
                break
            if temp[2][0] == temp[0][2] and temp[0][2] != 0:
                flag = True
                break
            temp[1][1] = masu[1][1]
        elif num == 5:
            if temp[1][0] == temp[1][1] and temp[1][0] != 0:
                flag = True
                break
            if temp[0][2] == temp[2][2] and temp[0][2] != 0:
                flag = True
                break
            temp[1][2] = masu[1][2]
        elif num == 6:
            if temp[0][0] == temp[1][0] and temp[1][0] != 0:
                flag = True
                break
            if temp[2][1] == temp[2][2] and temp[2][2] != 0:
                flag = True
                break
            if temp[0][2] == temp[1][1] and temp[0][2] != 0:
                flag = True
                break
            temp[2][0] = masu[2][0]
        elif num == 7:
            if temp[0][1] == temp[1][1] and temp[0][1] != 0:
                flag = True
                break
            if temp[2][0] == temp[2][2] and temp[2][0] != 0:
                flag = True
                break
            temp[2][1] = masu[2][1]
        else:
            if temp[0][0] == temp[1][1] and temp[0][0] != 0:
                flag = True
                break
            if temp[2][1] == temp[2][0] and temp[2][0] != 0:
                flag = True
                break
            if temp[0][2] == temp[1][2] and temp[0][2] != 0:
                flag = True
                break
            temp[2][2] = masu[2][2]

    if flag: 
        cnt += 1

print('{:.10f}'.format(1.0 - cnt/362880))