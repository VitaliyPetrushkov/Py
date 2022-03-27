my_list = input('Введите список через пробел: ').split()
for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]
print(' '.join([str(el) for el in my_list]))