import random   # импорт модуля random
import string   # импорт модуля string

def get_random_password(n=5) -> str:    # ввод функции рандомного пароля

    d = string.digits + string.ascii_lowercase + string.ascii_uppercase    # создание алфавита - строка, состоящая из букв верхнего и нижнего регитсра и цифр, - с помощью модуля string
    return random.sample(d, k=n)    # возврат 5-значного (по умоляанию) пароля

print(get_random_password())
