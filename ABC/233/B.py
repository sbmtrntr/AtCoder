l, r = map(int, input().split())
s = input()

l, r = l-1, r-1
hanten = ""

for i in range(r-l+1):
    hanten += s[r-i]

print(s[:l] + hanten + s[r+1:])