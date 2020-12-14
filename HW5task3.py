with open('ЗПсотрудников.txt', 'r', encoding='utf-8') as f:
    sal = []
    poor = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 у сотрудника по фамилии {poor}. Средний оклад составляет: {sum(map(int, sal)) / len(sal)}')