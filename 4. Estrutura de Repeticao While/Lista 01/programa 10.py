a = 3
c = a + 2
while a <= 6:
    b = a - 2
    print(b)
    while (b > 0):
        if a < c:
            c = a * 2
        elif a > 3:
            c = a + b
        else:
            c = b - 1
        print(c)
        b -= 2
    a += 3
