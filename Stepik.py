#Разложение числа
x=int(input("введите число:"))
a=x//10000
b=x//1000%10
c=x//100%10
d=x//10%10
e=x%10
print(a,b,c,d,e,sep='')

#Как проверить числа на положительность или ОТРИЦАТЕЛЬНОСТЬ
x=int(input())
print(x>0)

#Как проверить число на четность или нечетность (Если хотим проверить на кратность другие числа,то ставим их вместо 2)
x=int(input())
print(x%2==0)

#Проверка на двузначность или трехзначность:
x=int(input())
print(x>= 100 and x<=999)



#Очередность выполнения союзов
not #1
and #2
or  #3


 #Математические формулы
import math #запускает библиотеку математических формул
math.trunc(32.3) #отсекает дробную чать числа = 32
math.floor() # округление вниз, (если работать с минусовыми то оно будет увиличивать)
math.ceil() #округление вверх, (если работать с минусовыми то оно будет уменьшать)
1. Функция trunc - является частью модуля math. Отсекает дробную часть от числа. Фактически, проще использовать встроенную функцию приведения типов int, так как её подгружать через модуль не нужно.
Примеры:
from math import trunc
print(trunc(2.5)) # 2
print(trunc(3.5)) # 3
print(trunc(-2.5)) # -2

print(int(2.5)) # 2
print(int(3.5)) # 3
print(int(-2.5)) # -2

2. Функция floor - является частью модуля math. Округляет числа в сторону минус бесконечности (вниз).
Примеры:
from math import floor
print(floor(2.5)) # 2
print(floor(3.5)) # 3
print(floor(-2.5)) # -3

3. Функция ceil - является частью модуля math. Округляет числа в сторону плюс бесконечности (вверх).
Примеры:
from math import ceil
print(ceil(2.5)) # 3
print(ceil(3.5)) # 4
print(ceil(-2.5)) # -2

4. Функция round - является встроенной функцией, которую не нужно подгружать. Она похожа на "школьное округление", но у неё есть своя особенность:
Числа с дробной частью от 0 до 0.5 (не включая 0.5) - round округляет вниз.
print(round(5.3)) # 5
Числа с дробной частью от 0.5 (не включая 0.5) до 1 - round округляет вверх.
print(round(6.7)) # 7
Числа с дробной частью 0.5 - round округляет до ближайшего целого чётного числа.
print(round(12.5)) # 12
print(round(13.5)) # 14

П.с.: "школьное" округление (если дробная часть от 0 до 0.5 (не включая 0.5) - округление вниз, а если от 0.5 до 1 - округление вверх) - это Российский стандарт и в Питон его не закладывали, поэтому приходится самим его реализовывать, вот код:

from math import floor, ceil
N = float(input())
if N - int(N) < 0.5:
    print(floor(N))
else:
    print(ceil(N))

П.с.с.: Ребята, не используйте (по возможности) конструкцию "from math import *", так как при дальнейшей работе с программами вы будете использовать ни одну библиотеку и в разных библиотеках есть функции, которые называются одинаково, а выполняют разные действия! (Что вызывает немало конфликтов в работе программ) Лучше используйте from math import (Функции через запятую) и пишите те функции, с которыми точно будете работать.

while #
for для каакого-то набора данных в чем либо:
for x#для чего in var_1: #откуда брать инфу
#Фунция проходится по каждому символу из var_1

s = """ ывыв """
print(s)
""" Служебные символы:
\newline игнорируется (продолжение на новой строке) 
\\ символ обратного слеша (остается символ \ )
\' Апостроф ( остается один символ')
\" Кавычка (остается один символ ')
\a Звонок
\b Забой
\f Перевод формата
\n Новая строка(перевод строки)
\r Возврат каретки
\t Горизонтальная табуляция
\v Вертикальная табуляция
"""
print('/\_/\ \n>^,^< \n / \ \n(|_|)_/ \n') #мой кот


