'''
Задана рекуррентная функция.
Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
В-21.   F(0) = F(1) = 1, F(n) = F(n–1)*5, при n > 1
'''

import time
import matplotlib.pyplot as plt

def accept_number(description):
    while True:
        try:
            return int(input(description))
        except ValueError:
            print('Введенное значение не является числом.')

def F_rec(n):               # Рекурсивная функция
    if n == 1:
        return 1
    else:
        return 5 * F_rec(n-1)

def F_iter(n):              # Итеративная функция
    result = 1
    for i in range(2, n+1):
        result *= 5
    return result

n = accept_number("Введите натуральное число n, для подсчета F(n) = F(n–1) * 5: ")

while n < 2:  # ошибка в случае введения не натурального числа
    n = int(input("\nВы ввели не подходящее число. Введите число >1 :\n"))

# Подсчёт времени выполнения рекурсивно
start_time = time.time()
f_rec = F_rec(n)
end_time = time.time()
recursive_time = end_time - start_time

# Подсчёт времени выполнения итеративно
start_time = time.time()
f_iter = F_iter(n)
end_time = time.time()
iterative_time = end_time - start_time

# Вывод
print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(n, f_rec, recursive_time))
print("F({}) = {} (итеративно в {:.6f} секунд)".format(n, f_iter, iterative_time))

# График
recursive_times = []  # создание списков для дальнейшего построения таблицы
recursive_values = []
iterative_times = []
iterative_values = []
n_values = list(range(1, n + 1, +1))

for n in n_values:  # заполнение списков данными
    start = time.time()
    recursive_values.append(F_rec(n))
    end = time.time()
    recursive_times.append(end - start)

    start = time.time()
    iterative_values.append(F_iter(n))
    end = time.time()
    iterative_times.append(end - start)

table=[]
for i, n in enumerate(n_values):
            table.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])
print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))        # вывод таблицы
print('-' * 160)
for j in table:
    print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format(j[0], j[1], j[2], j[3], j[4]))

plt.plot(n_values, recursive_times, label='Рекурсия')  # вывод графиков
plt.plot(n_values, iterative_times, label='Итерация')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.title('Сравнение рекурсивного и итерационного подхода')
plt.legend()
plt.show()

print("\nРабота программы завершена.\n")