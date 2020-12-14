def summary():
    try:
        with open('summa.txt', 'w+') as f:
            line = input('Введите цифры через пробел: ')
            f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()