# введем переменные для дальнейших вычислений
a = 0
b = ''
# ввод первого значения
c = int(input())
# пока введенное значение неравно 0, будет выполняться цикл
while c != 0:
    # чтобы найти наибольший элемент, нужно добавить это условие, которое будет его находить
    if a < c:
        a = c
    # сделаем строку из всех значений, чтобы в дальнейшем найти сколько раз встречается наибольший элемент
    b += str(c)
    # повторный ввод значений
    c = int(input())
# теперь я использую метод count, чтобы подсчитать сколько раз встречалось число а в b
print(b.count(str(a)))