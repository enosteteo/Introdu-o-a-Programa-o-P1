b = 5
c = 1
a = b + c
d = b - c
while b > 1:
    d = b - c + 1
    while d > 1:
        if d >= 3:
            a = c + 1
        else:
            a += 4
        d -= 2
    b -= 2
c = a + b + d