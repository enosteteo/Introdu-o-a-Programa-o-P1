a = 20
b = 8
c = a - b
while c > 1:
    a -= 4
    b += 1
    if b > 12:
        c -= 1
    elif a < 6:
        c -= 2
    else:
        c -= 3
b /= a
a = (c + b) / a