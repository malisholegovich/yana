a=input('Введите строку через пробелы ')
a=a.split()
print(a[::-1]) #Задача 1 скрин 4,1

def change(lst):
    p = lst.pop()
    e = lst.pop(0)
    lst.append(e)
    lst.insert(0, p)
    return lst
print(change([2,4,5,7,8])) #Задача 2 скрин 4,1


def to_list(*args):
    return list(args)
print(to_list(a)) #Задача 3 скрин 4,1


def useless(lst):
    return max(lst)/len(lst)
print(useless([3,5,1,2])) #Задача 4 скрин 4,1


def list_sort(lst):
    a.sort()
    return lst
print(list_sort(a)) #Задача 5 скрин 1, 5


def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"
print(to_float(12)) #задача 1 скрин 2



def avg_5(a1, b, c, d):
    return round((a1 + b + c + d) / 4, 5)
print(avg_5(1,5,9,2)) #задача 2 скрин 2


def mul_to_int(a, b):
    r = a * b
    if r % 1 == 0:
        return int(r)
    else:
        return float(r)
print(mul_to_int(12,67)) #Задача 3 скрин 2



v=int(input('Объем '))
pi=3.14
r = ((3 * v / (4 * pi)) ** (1/3))
print(r) #Задача 4 скрин 2

we=int(input('Число:'))
def dislike_6(n):
    if n == 6:
        return False
    else:
        return True
print(dislike_6(we)) #Задача 1 скрин 3

mk=input('Выберете к, а, д, м: ')
def help_bool(letter):
    if letter == 'к':
        return "Логическая операция 'И' (AND) является коммутативной."
    elif letter == 'а':
        return "Логическая операция 'ИЛИ' (OR) является ассоциативной и коммутативной."
    elif letter == 'д':
        return "Логическая операция 'ИЛИ' (OR) дистрибутивна относительно логической операции 'И' (AND)."
    elif letter == 'м':
        return "Правило де Моргана утверждает, что отрицание всей логической операции эквивалентно операции с каждым отрицанием отдельного операнда и изменением операции на противоположную."
    else:
        return "Выберете одну из 4 букв: к, а, д, м для получения справки по свойствам логических операций."
print(help_bool(mk))  #Задача 2 скрин 3


def to_dict(lst):
    di = {}
    for i in lst:
        di[i] = i
    return di
tt=to_dict(a)
print(tt) #Задача 1 скрин 6



n1=input('Имя ')
a11=input('Ворзраст ')
c1=input('Город проживание ')
big_slovari={'first_one':'we can do it'}
def biggest_dict(**kwargs):
    big_slovari.update(**kwargs)
biggest_dict(name=n1, age=a11, city=c1)
print(big_slovari) #Задача 2 скрин 6


dict = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5'}
keys = list(dict.keys())
first_key, last_key = keys[0], keys[-1]
dict[last_key], dict[first_key] = dict[first_key], dict[last_key]
del dict[keys[1]]
dict['new_key'] = 'new_value'
print(dict) #Задача 4 скрин 6





