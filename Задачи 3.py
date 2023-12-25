pleer1=input('Камень, ножницы, бумага:' )
pleer2=input('Камень, ножницы, бумага:' )
def play(pleer1, pleer2):
    if "камень" == pleer1:
        return "Победил первый игрок" if "ножницы" == pleer2 else "Победил второй игрок"
    if "ножницы" == pleer1:
        return "Победил первый игрок" if "бумага" == pleer2 else "Победил второй игрок"
    if "бумага" == pleer1:
        return "Победил первый игрок" if "камень" == pleer2 else "Победил второй игрок"
    if pleer1 == pleer2:
        return "Ничья"
print(play(pleer1, pleer2)) #скрин 1


def coins(money_bag):
    total_money = sum(money_bag)
    if total_money % 3 == 0:
        return True
    else:
        return False
coins1 = [1, 2, 3, 4, 5]
print(coins(coins1)) #Скрин 10


zzz=input("Предложение с большим кол-во ? или !: ")
def yell(u, i):
    while u[-1]==i:
        u = u[:-1]
    return u + i
def no_yell(u):
    if u[-1]=='!':
        return yell(u, '!')
    if u[-1]=='?':
        return yell(u, '?')
    return(u)
print(no_yell(zzz)) #Скрин 2


def ochki21(cards):
    summa = 0
    for i in cards:
        if i in ['В', 'Д', 'К']:
            summa += 10
        elif i == "Т":
            summa += 1
        else:
            summa += i
    if summa > 21:
        return True
    return False
print(ochki21([2,8,3,'Т'])) #скрин 3



ttimee=input('Введите время как в примере - 00:00 am(если pm то просто время без am/pm: ')
def amvspm(time):
    if "am" in time:
        if time == "12:00 am":
            return "0:00"
        else:
            return time.replace(" am", "")
    elif "pm" in time:
        if time == "12:00 pm":
            return "12:00"
        else:
            time = time.replace(" pm", "")
            time = time.split(":")
            hour = int(time[0])
            minut = time[1]
            h24 = str(hour + 12)
            return f"{h24}:{minut}"
    else:
        if int(time.split(":")[0]) < 12:
            if time == "00:00":
                return "12:00 am"
            else:
                return time + " am"
        else:
            time = time.split(":")
            h24 = int(time[0])
            h = str(h24 - 12)
            return f"{h}:{time[1]} pm"
print(amvspm(ttimee)) #скрин 6

#Скрин 7. Я не знаю как решить эту задачу без условий, за которые даются баллы



def numtoruss(num):
    l1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    l2 = ['одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнцадцать', 'шестьнадцать', 'семнадцать',
          'восемнадцать', 'девятнадцать']
    l3 = ['двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ', 'семьдесят ', 'восемьдесят ', 'девяносто ']
    l4 = ['сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ', 'семьсот ', 'восемьсот ', 'девятьсот ']
    if num == 0:
        return 'ноль'
    a = num // 100
    b = num % 100
    c = b // 10
    d = b % 10
    ress = ''
    if a != 0:
        ress += l4[a - 1]
    if c != 0:
        if c == 1:
            ress += l2[d - 1]
            return ress
        else:
            ress += l3[c - 2]
    if d != 0:
        ress += l1[d - 1]
    return ress
print(numtoruss(500)) #скрин 8



def lucky(tikets):
    lst = [0] * (tikets // 2 * 10 + 1)
    lst[0] = 1
    for n in range(1 + tikets // 2):
        for i in range(min(tikets // 2 * 10, n * (10 - 1)), 0, -1):
            lst[i] = sum(lst[max(0, i + 1 - 10): i + 1])
    lst = [i ** 2 for i in lst]
    return sum(lst)
print(lucky(4)) #скрин 9






