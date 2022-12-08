from pprint import pprint   # импорт модуля pprint

list_dict = []  # ввод пустого списка словарей

pprint([{'bin': bin(d), 'dec': d, 'hex': hex(d), 'oct': oct(d)} for d in range(16)])
# вывод в столбик (с помощью pprint) списка словарей со значениями чисел до 15 включительно в разных системах исчесления с помощью list comrehension)
