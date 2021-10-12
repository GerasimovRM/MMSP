# Пользователь вводит число n. Нужно создать список от 0 до n включая
"""
n = int(input())
lst = []
for i in range(n + 1):
    lst.append(i ** 2)
"""
lst = [i ** 2 for i in range(int(input()) + 1)]
print(lst)
