# ДЗ на четверг (Ivanov_Lesson_15.py)
# №1. 1)Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# 2) Если список, то посчитать кол-во букв и чисел в нём.
# 3) Число – кол-во нечётных цифр.
# 4) Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой
#
# Сбарсываем ссылку на файл в репозитории

def print_type_data(fn):
    def wrapper(arg):
        print(f'Тип отправленных данных {type(arg)}')
        fn(arg)

    return wrapper


@print_type_data
def functions(ar):
    sumNum = 0

# 1
    if isinstance(ar, tuple):
        for i in ar:
            if isinstance(i, str):
                sumNum += len(i)
        print(f'Длина всех строк в кортеже {sumNum}')
# 2
    elif isinstance(ar, list):
        chars = 0
        nums = 0
        for i in ar:
            if isinstance(i, str):
                for j in i:
                    if str.isalpha(j):
                        chars += 1
                    elif str.isdigit(j):
                        nums += 1
            elif isinstance(i, int):
                nums += 1
        print(f'Количество букв и чисел в списке {chars, nums}')
# 3
    elif isinstance(ar, int):
        nums = 0
        while ar > 0:
            if (ar % 10) % 2 != 0:
                nums += 1
            ar = (ar - ar % 10) // 10
        print(f'Колличество нечетных цифр в числе {nums}')
#4
    elif isinstance(ar, str):
        chars = 0
        for i in ar:
            if str.isalpha(i):
                chars += 1
        print(f'Количество букв в строке {chars}')

    else:
        print('Введен другой тип данных')


functions(('shfd', 'qwhn', 1, 2, 'hrt', 7, 'reee'))
functions(['shfd', 'qwhn1', 1, 2, 'hrt', 7, 'reee'])
functions(1234)
functions('кол-во1 букв!')
functions({1: 'a', 2: 'b'})
