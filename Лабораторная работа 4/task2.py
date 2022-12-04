def get_count_char(str_):
# TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.split()) # избавляюсь от пробелов
    str_ = str_.lower() # привожу все к нижнему регистру
    str_ = "".join(letter for letter in str_ if letter.isalpha()) # эту строку подсмотрел в интернете, так как не смог сам избавиться от пунктуации

    dict_ = {} # ввожу словарь

    for letter in str_: # запускаю цикл для каждой буквы
        if letter in dict_:
            dict_[letter] += 1 # увеличиваю значение на 1, если буква уже встречалась в словаре
        else:
            dict_[letter] = 1 # оставляю значение неизменным, пока буква не встретится еще раз

    return dict_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

print(get_count_char(main_str))
