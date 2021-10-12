lst = [1, 2, 3.5, True, None, [4, 5, 6]]
print(lst)

# обращение по индексу
print(lst[0], lst[1], lst[-1])
# операция среза
print(lst[:3])
print(lst[::2])
print(lst[::-1])

# изменение элемента по индексу
lst[3] = 55.5
print(lst)

# небольшой пример
a = [1, 2, 3]
b = a
print(id(a), id(b))
b[0] = 4
print(a)  # [4, 2, 3]

# сравнение списков
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b, a == c)  # сравнение по значению
print(id(a), id(b), id(c))
print(a is b, a is c)  # сравнение по id объекта


# заполнение пустого списка
lst = []  # lst = list()
lst.append(10)
lst.append(20)
print(lst)
lst.extend([50, 60])
print(lst)
lst.append([80, 90])
print(lst)
lst.insert(0, 100)
print(lst)


# пробежать по списку
for i in range(len(lst)):
    print(lst[i])

for elem in lst:
    print(elem)
