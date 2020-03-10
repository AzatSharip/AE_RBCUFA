data_list = list()
with open("C:/Users/-/YandexDisk-az.sharip/AE expressions/data_grf/Grafik.txt") as f:
    line = f.readlines()

    # Цикл добавляет нужные значения в список
    for i in range(1, 11):
        val = float(line[i].split(',')[-1])
        data_list.append(val)
print(data_list)
list = data_list
max_num = max(list)
min_num = min(list)


index_min_max = max_num - min_num
list2 = [((max_num - elements) * 100) / index_min_max for elements in list]
list3 = [100 - elements for elements in list2]
list4 = [round(elements, 1) for elements in list3]

# print(list2)
# print(list3)
# print(list4)
with open("C:/Users/-/YandexDisk-az.sharip/AE expressions/data.txt", 'w') as file:
    i = 1
    for elements in list4:
        print('var y{} = ["{}"];'.format(i, elements))
        file.write('var y{} = ["{}"];'.format(i, elements))
        i = i + 1

    var_max = max(list4)
    print('var max = ["{}"];'.format(var_max))
    file.write('var max = ["{}"];'.format(var_max))


