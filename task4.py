# ввод значения
z = int(input())
c = int(input())
# добавим переменную, для записи максимальной длины монотонности
maxx = 1
# пока не введется 0
#
while c != 0:
    while z == c and c != 0:
        y = 1
        z = c
        c = int(input())
    y = 1
    while z < c and c != 0:
        y += 1
        if y > maxx:
            maxx = y
        z = c
        c = int(input())
    y = 1
    while z > c and c != 0:
        y += 1
        if y > maxx:
            maxx = y
        z = c
        c = int(input())

    # теперь переопределим z, чтобы она стала предыдущим значением
# вывод длины монотонности
print(maxx)