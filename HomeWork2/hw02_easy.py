# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print('Задача-1:')
p = list()
p = "яблоко", "банан", "киви", "арбуз", "грейпфрут"
t = len(str(p[1]))
for i in p:
    if t < len(str(i)):
        t = len(str(i))
j = 1
k = str(' ')
for i in p:
    g = 0
    while g <= t - len(i):
        k += ' '
        g += 1
    print('{}.{}{}'.format(j, k, i))
    j += 1
    k = ' '
print()
# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
print('Задача-2:')
# s1 = list()
# s2 = list()
s1 =['1', '2', '3', '4', '5', '3', '4', '4']
print('Дано s1: ', s1)
s2 = ['3', '4']
print('Дано s2: ', s2)
for i in s2:
    for j in range(s1.count(i)):
        s1.remove(i)
print('Итоговый s1: ', s1)
print()
# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print('Задача-3:')
s1 =[1, 2, 3, 4, 5, 3, 4, 4]
print('Дано s1: ', s1)
s2 = []
for i in s1:
    if i % 2 == 0:
        s2.append(i/4)
    else: s2.append(i*2)
print('s2: ', s2)