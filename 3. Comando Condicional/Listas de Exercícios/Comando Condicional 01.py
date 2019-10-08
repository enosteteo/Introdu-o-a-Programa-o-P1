# Programa 01

a = 5
b = 2
if(a+b < 10):
    c = a-b
else:
    c = a+b
a = c*b
print(b-3)

# Programa 02

a = 1
b = 0
if (a > 0):
    b = a + b
    c = b + b
    a = a + b + c
else:
    b = 2 * a
print(a + 3)

# Programa 03

a = 2
b = 7
if (a + b > 10):
    c = a + 1
    b = c + 1
else:
    c = a – 1
    b = c – 1
    a = b – 1

# Programa 04

a = 8
b = a + 3
c = b – 1
if (c > 4):
    a = a + c
else:
    a = a + b
b = (2 * c) – a
c = a – c
a = c / b

# Programa 05

b = 5/2 + 6/4
a = 3 + b
if (a > 7):
    c = a + c
    print(b – a)
elif (a == 7):
    c = a – b
    print(2*c + 1)
else:
    a = a + b

# Programa 06

a = – 5
b = 9
if (a + b == 3):
    c = a + 7
    d = b – 4
else:
    c = a + 2
    d = b – 10
a = –2 * a
b = – b / c
c = c + 4
d = d + c

# Programa 07

a = 3
b = 2
c = 4
if (a + b + c < 7):
    b = c + 5
    c = a + 8
    a = (a * c) + b
else:
    b = 5 * c
    c = a + b – 8
    a = (2 * a) – 1
b = b – (a + c)
c = c – (a + b)

# Programa 08

a = 6
b = 1
if (a > 0):
    if (b > 0):
        c = a + b
    else:
        c = a - b
elif (b < 5):
    c = a * b
else:
    c = a / b

# Programa 09

a = 1
b = 3
if (a > 0):
    if (b > 0):
        c = (a + b) * 2
    else:
        c = 0
else:
    b = 2
if (c > 0):
    a = 2
else:
    b = 4

# Programa 10

c = 4
b = c * 5/2
a = c * b – b
if (b > a):
    if (c > b):
        d = a * 2
    elif (a > c):
        d = 29 – a + b
elif (a > b + c):
    d = (b – c)/3
    print(a + d)
else:
    d = c – 9 + a
a = a – (b + c + d)

# Programa 11

d = 6**2 – 8
if (d > 20):
    if (d < 25):
        a = d / 3
        print(a + d)
    elif (d > 28):
        a = d*5 + 1
        print(a – d)
    elif (d < 22):
        b = d + 1
        print(b – 3)
    else:
        b = d / 7
        print(b**2)
a = d – b

# Programa 12

c = 7 + 5*1.2
b = c – 4
if (b > 9):
    if (c == 10):
        a = b + 3
    elif (b == 6):
        a = c*3
        print(a – c)
elif (c >= 13):
    a = b + 1
else:
    a = c / 7
    print(a**b)
if (a < b):
    a = c – b
c = c – a

# Programa 13

b = 5
if (b > 7):
    a = b + 4
    c = a * 2
a = (b – 2) ** 3
if (a < 15):
    d = c – a
    print(a)
elif (a > 29):
    if (b > 8):
        d = b + c – 1
    elif (b < 6):
        d = a * c
else:
    a = a + 2 * b
