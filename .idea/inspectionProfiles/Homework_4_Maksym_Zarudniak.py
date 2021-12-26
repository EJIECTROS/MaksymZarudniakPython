n = input('Введите номер: ')  # Ввод
def vhod(n):
    if len(n) == 8:  # Проверяла на соответствие Длине введенного текста
        print('Yes, length number is equal to 8')
        return n[0:2], n[2], n[3], n[4], n[5], n[6:8]  # Возвращала 6 значений полученных из введенного номера (по 2 буквы и 4
    else:
        return False  # Если общее количество символов больше или меньше 8 (во введенных данных) возвращала False
i = vhod(n)
print(i)


def summm(n):
    c_count = int(n[2]) + int(n[3]) + int(n[4]) + int(n[5])
    return c_count
b = summm(n)
print(b)


