f_name = input('Запишите данные в файл: ')
f = open("ПриветМир.txt", 'w+')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()
