my_list = input('Введите список через пробел: ').split()
for n, v in enumerate(my_list, 1):
   print(f'{n}) {v[:10]}')