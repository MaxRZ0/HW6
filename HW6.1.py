# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

f_elem = int(input())
step = int(input())
quantity_num = int(input())

def proggres_ar(f_elem, step, quantity_num):
    ar_prog = f_elem
    prog_array = [f_elem]
    for i in range(quantity_num-1):
        ar_prog += step
        prog_array.append(ar_prog)
    return prog_array

print(proggres_ar(f_elem, step, quantity_num))
