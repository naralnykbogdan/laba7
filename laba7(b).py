# Задача. Вивести дані про книги, в яких кількість сторінок більше 150. Поля
# структури: Автор, Кількість сторінок, Тираж, Рік видання.

while True:
    while True:
        try:
            x = int(input('Введіть номер з 1 книжки: '))
            y = int(input('Введіть номер з 2 книжки: '))
            z = int(input('Введіть номер з 3 книжки: '))
            break
        except ValueError :
            print('Введіть номер: ')
    keys=['автор','тираж','видання','к-ть сторінок']
    a = [input('Введіть автора 1 книжки: '), int(input('Введіть тираж 1 книжки: ')), int(input('Введіть видання 1 книжки: ')), x]
    b = [input('Введіть автора 2 книжки: '), int(input('Введіть тираж 2 книжки: ')), int(input('ВВедіть видання 2 книжки: ')), y]
    c = [input('Введіть автора 3 книжки: '), int(input('Введіть тираж 3 книжки: ')), int(input('Введіть видання 3 книжки: ')), z]
    info1 = {keys: a for(keys, a) in zip(keys, a) if x > 150}
    info2 = {keys: b for(keys, b) in zip(keys, b) if y > 150}
    info3 = {keys: c for(keys, c) in zip(keys, c) if z > 150}
    print(info1,info2,info3)
    result = input('Хочете повторити?Якщо так  - 1, якщо рі - інше: ')
    if result == '1':
        continue
    else:
        break
