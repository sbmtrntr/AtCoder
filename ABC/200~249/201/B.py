N = int(input())

mountain = []
for i in range(N):
    s, t = input().split()
    t = int(t)
    mountain.append([s, t])

iti = ["", 0]
ni = ["", 0]

for i in range(N):
    if mountain[i][1] > iti[1]:
        ni = iti
        iti = mountain[i]
    
    elif mountain[i][1] > ni[1]:
        ni = mountain[i]

print(ni[0])
