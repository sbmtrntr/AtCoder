x, a, d, n = map(int, input().split())

if d < 0:
    a, d = a+(n-1)*d, -d

elif d == 0:
    print(abs(x-a))
    exit()

i = (x-a)//d

if i > n:
    print(x-(a+(n-1)*d))
elif i < 0:
    print(a-x)
else:
    print(min(abs(x-(a+i*d)), abs(x-(a+(i+1)*d))))




""" left = 0
right = n-1

while left <= right:
    mid = (left + right)//2
    if x > a + mid*d:
        left = mid+1
    else:
        right = mid-1

if x < a or x > a + (n-1)*d:
    print(min(abs(x - a), abs(x - (a+(n-1)*d))))
    exit()

else:
    print(x-(a + right*d)) """
    

"""
y = min(abs(x-a), abs(x-a-d))

if d == 0:
    print(abs(a-x))
    exit()

if y == abs(x-a):
    print(y)
    exit()

m = (x-a)//d
if m > n:
    print(abs(x-(a + n*d)))
else:
    print(min(abs(x-(a + m*d)), abs(x-(a + (m-1)*d)), abs(x-(a + (m+1)*d))))
"""