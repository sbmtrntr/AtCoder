N = int(input())
S = list(input())

for i in range(N-2):
    if "".join(S[i:i+3]) in ["RRR", "BBB"]:
        print("Yes")
        exit()
print('No')