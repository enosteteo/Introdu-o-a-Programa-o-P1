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
    c = a + b - 8
    a = (2 * a) - 1
b = b - (a + c)
c = c - (a + b)