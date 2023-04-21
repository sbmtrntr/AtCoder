N = int(input())

if N >= 42:
    print("AGC" + "0" + str(N+1))
else:
    if len(str(N)) == 2:
        print("AGC" + "0" + str(N))
    else:
        print("AGC" + "00" + str(N))
    