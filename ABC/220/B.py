K = int(input())
A, B = input().split()

dec_A = 0
dec_B = 0
for i in range(len(A)):
    dec_A += int(A[len(A)-1-i]) * K**i

for i in range(len(B)):
    dec_B += int(B[len(B)-1-i]) * K**i

print(dec_A*dec_B)