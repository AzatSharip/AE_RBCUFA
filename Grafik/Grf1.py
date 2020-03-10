f = open('C:/Users/Азат/YandexDisk-az.sharip/AE expressions/data_grf/GAZP_200229_200310.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end = '')
f.close()



#
#
#
# list = [155, 156, 169, 165, 180, 185, 184, 188, 191, 191]
# max_num = max(list)
# min_num = min(list)
#
#
# index_min_max = max_num - min_num
# list2 = [((max_num - elements) * 100) / index_min_max for elements in list]
# list3 = [100 - elements for elements in list2]
# list4 = [round(elements, 1) for elements in list3]
#
#
# # print(list2)
# # print(list3)
# # print(list4)
# f = open('C:/Users/Азат/YandexDisk-az.sharip/AE expressions/data.txt', 'w')
# i = 1
# for elements in list4:
#     print('var y{} = ["{}"];'.format(i, elements))
#     f.write('var y{} = ["{}"];'.format(i, elements))
#     i = i + 1
#
#
# var_max = max(list4)
# print('var max = ["{}"];'.format(var_max))
# f.write('var max = ["{}"];'.format(var_max))
#
#
# # f = open('C:/Users/Азат/YandexDisk-az.sharip/AE expressions/data.txt', 'w')
# # f.write(poem)
# f.close()