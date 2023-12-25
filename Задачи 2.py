g=input()
def double_letters(word):
    for i in range(1,len(word)):
        if word[i]==word[i-1]:
            return True
    else:
        return False
print(double_letters(g)) #скрин 12



def osi(x, y):
    r = []
    for a, b in zip(x, y):
        r.append([a, b])
    return r
print(osi([1,4,8,9],[4,7,2,8])) #скрин 10



ee=input()
j=input()
def hello_people(names):
    yy = ""
    if names:
        for i in names:
            yy += "Привет "+i+", "
        yy = yy[:-2:]
    return(yy)
print(hello_people([ee,j])) #скрин 11

oo=input('Любое предложение с большой длинной пробелов: ')
def no_probels(sentence):
    rr = ""
    for i in sentence.split(" "):
        if i != "":
            rr += i + " "
    return(rr[:-1:])
print(no_probels(oo)) #скрин 13

pi=3.14
r=int(input('Радиус цилиндра: '))
h=int(input('Высота цилиндра: '))
def obiom(r, h):
    w = pi * r ** 2   *  h  /  1000
    return round(w, 2)
print(obiom(r,h))  #скрин 14



def umnogenie(numbers):
    p = 1
    for x in numbers.split(', '):
        p *= int(x)
    return p
print(umnogenie("2, 3, 345, 90586")) #скрин 15




def oosi(a, b):
    x1 = a["x"]
    y1 = a["y"]
    x2 = b["x"]
    y2 = b["y"]
    ab = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(ab, 3)
print(oosi({"x": 98, "y": 12}, {"x": 4, "y": 3})) #скрин 17



f=input()
def yazik(text):
    for i in range(len(text)):
        if text[i] == 'х':
            text = text.replace(text[i], '4')
        elif text[i] == 'к':
            text = text.replace(text[i], '3')
        elif text[i] == 'р':
            text = text.replace(text[i], '4')
    return text
print(yazik(f)) #скрин 18



def mediana(number_list):
    number_list.sort()
    n = len(number_list)
    if n % 2:
        return number_list[n // 2]
    else:
        return (number_list[n // 2] + number_list[n // 2 - 1]) / 2
print(mediana([7323, 6346, 0, 36457, 57, 7])) #скрин 21


str=input()[::-1]
str=str.swapcase()
print(str)  #скрин 8


x=int(input('Сколько врагов?'))
list=' '
for i in range(x):
    a=input()
    list=list+a+' '
print(list)
d=int(input('Сколько друзей?'))
list1=[]
for i in range(d):
    h=input()
    list1=list1+[h]
print(list1)
print('Удаление врагов....')
result = []
for i in list:
    if i not in list1:
        result.append(i)
print(result) #скрин 9
















