# ввод значений
a = int(input())
# обозначим переменные, которые будут помогать в счете
i = 1
summa = 0
# пока i * i <= a, то будет выполняться цикл
while i * i <= a:
    # если а делится без остатка на i,
    # то нужно проверить будет ли равно числу а произведение i само на себя и если это так,
    # то нужно прибавить к сумме только 1, т к i умножается само на себя
    if a % i == 0:
        if i * i == a:
            summa += 1
        # иначе прибавить 2 т к есть и делитель и частное, которое получилось при делении числа а на i
        else:
            summa += 2
    # прибавим 1 к i, чтобы увеличить делитель на один
    i += 1
# вывод количества делителей
print(summa)
