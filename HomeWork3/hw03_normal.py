# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('Задача-1:')
# ns = list()
# ns = [0, 1, 1]
# print(type(ns))
# print(ns[1-2])
def fibonacci(n,m):
    ns = [0, 1, 1]
    nr = []
    st = str()
    for i in range(3,m+1):
        ns.append(ns[i-2] + ns[i-1])
    for i in range(n, m+1):
        nr.append(ns[i]) # возвращает список с диапазоном последовательности.
        st += str(ns[i])
        st += ' '
    return st # можно список nr  выводить
print(fibonacci(1,10))
print()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('Задача-2:')
def sort_to_max(origin_list):
    ol = origin_list
    ols = []
    for i in range(len(ol)):
        ol.pop([i])

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

