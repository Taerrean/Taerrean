from math import ceil
a = int(input())
b = int(input())
c = int(input())
n = int(input())
l = 0
r = n
while l != r:
    m = ceil((l + r)/2)
    z2 = (a + m)/2 - b
    z3 = (a + m)/2 - c
    if m + z2 + z3 <= n:
        l = m
    else:
        r = m - 1
if (a + l) % 2 == 0:
    p1 = l
    p2 = (a + l)//2 - b
    p3 = (a + l) // 2 - c
else:
    p1 = l - 1
    p2 = (a + l - 1)//2 - b
    p3 = (a + l - 1) // 2 - c
if p2 >= 0 and p3  >= 0:
    print(p1)
    print(p2)
    print(p3)
else:
    print(0)
