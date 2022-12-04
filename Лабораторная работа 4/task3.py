def delete(list_, index=-1):
# TODO реализовать функцию удаления элемента из списка по индексу

    left_list = list_[:index] # ввожу переменную левой части списка после слайсирования
    right_list = list_[index + 1:] # # ввожу переменную правой части списка после слайсирования
    clear_list = [] # # ввожу переменную пустой части списка после слайсирования (на случай ввода "index=-1")

    if index == -1:
        return left_list + clear_list # сложение двух частей при index=-1
    else:
        return left_list + right_list # сложение двух частей при отсальных случаях




print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
