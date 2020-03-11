import FinamParser




price_list = list()
day_mon_list = list()
with open("D:/Personal/GitHub/AE/Grafik/data_grf/Grafik.txt") as f:
    line = f.readlines()
    length = int(len(line))

    # Цикл обрабатывает текст в файле и добавляет нужные значения в список
    for i in range(1, length):
        val = float(line[i].split(',')[-1])
        price_list.append(val)

        day_mon_year = line[i].split(',')[2]
        day_mon = day_mon_year[:5]
        day_mon_list.append(day_mon)
    # print(day_mon_list)

list = price_list
max_num = max(list)
min_num = min(list)


index_min_max = max_num - min_num
list2 = [((max_num - elements) * 100) / index_min_max for elements in list]
list3 = [100 - elements for elements in list2]
list4 = [round(elements, 1) for elements in list3]

last_point = list[-1]
midle_num = max_num - ((max_num - min_num) / 2)
print(midle_num)
print(list, list2, list3, list4, sep='\n')
print(last_point)
print(FinamParser.ticker)

with open("D:/Personal/GitHub/AE/Grafik/data.txt", 'w') as file:

    #Цикл создает массив из значений y, который записывается в файл
    i = 1
    for elements in list4:
        file.write('var y{} = ["{}"];'.format(i, elements) + '\n')
        i = i + 1

    var_max = max(list4)
    file.write('var max = ["{}"];'.format(var_max) + '\n')

    file.write('var day_mon = {}'.format(day_mon_list) + '\n')

    file.write('var val_1 = ["{}", "{}", "{}", "{}"];'.format(min_num, max_num, midle_num, last_point) + '\n')

    file.write('var ticker = ["{}"];'.format(FinamParser.ticker) + '\n')

import BatRanner