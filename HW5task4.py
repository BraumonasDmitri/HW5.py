rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('numbers.txt', 'r') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('numbers1.txt', 'w') as file2:
    file2.writelines(new_file)