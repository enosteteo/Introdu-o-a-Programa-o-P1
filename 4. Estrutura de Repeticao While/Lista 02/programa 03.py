cont = 50
multi3 = 0
while cont > 0:
    num = int(input())
    if num % 3 == 0:
        multi3 += num
    cont -= 1
print(multi3)