import math

N = int(input())

for i in range(2,int(math.sqrt(N))+2):
    if N % i == 0:
        print("No")
        exit()
 
print("Yes")