import random   # импорт модуля random
from random import randint  # импорт функции randint из модуля random

def get_unique_list_numbers() -> list[int]: # ввод функции

    start = -10     # ввод переменной для граничных значений
    stop = 10       # ввод переменной для граничных значений
    count = 15      # ввод переменной для граничных значений

    list_digits = []    # ввод пустого списка

    for i in range(count):      # ввод пошагового цикла
        d = random.randint(start, stop)     # присваивание переменной d рандомное значение в установленных границах
        while d in list_digits:     # ввод цикла условия: пока значение числа в списке повторяется
            d = random.randint(start, stop)     # ввод действия: присваивание нового значения числу
        list_digits.append(d)   # список увеличивается на одно уникальное значение

    return list_digits      # возврат списка

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))    # проверка уникальности значений в списке
