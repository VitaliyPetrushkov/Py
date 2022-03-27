s = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг - {s}')
n = int(input('Введите новый элемент (выход - 0): '))
while n != 0:
    for el in range(len(s)):
        if s[el] == n or s[el] > n > s[el + 1]:
            s.insert(el + 1, n)
            break
        elif s[0] < n:
            s.insert(0, n)
        elif s[-1] > n:
            s.append(n)
    print(f'Текущий рейтинг - {s}')
    n = int(input('Введите новый элемент (выход - 0): '))