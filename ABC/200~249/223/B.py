S = input()

def left_shift(s):
    return s[1:] + s[0]

def right_shift(s):
    return s[-1] + s[:-1]

l = S
r = S
max_s = "a"
min_s = "z"
for i in range(len(S)):
    l = left_shift(l)
    r = right_shift(r)
    max_s = max(max_s, l, r)
    min_s = min(min_s, l, r)

print(min_s)
print(max_s)