my_list = (2, 34.5, 2 + 3j, 'str', None, True, set('выхухоль'), dict(k1='val1', k10='val10'), [
    2, 25.2, 'a'], tuple('что-то'))
print(my_list)
for el in my_list:
    print(f'{el} это {type(el)}')  # хотел выровнять по правому краю, не смог, ругался на None
