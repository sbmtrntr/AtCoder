"""
s = input()

for i in range(len(s)):
    if s[-1] == "a":
        s = s[:-1]


flag = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        flag = False
        break

if flag: print("Yes")
else: print("No")
"""


s = input()

x = 0
for i in range(len(s)-1):
    if s[i] == "a": x += 1
    else: break

y = 0
for i in range(len(s)):
    if s[len(s) - 1 - i] == "a": y += 1
    else: break

if len(s) == x: print("Yes")

flag = True
if x > y: 
    print("No")
    exit()
else:
    s = s[:len(s) - y + x]
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            flag = False
            break

if flag: print("Yes")
else: print("No")
