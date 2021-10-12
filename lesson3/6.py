# Пользователь вводит сначала n - количество данных, затем данные (целые числа).
# Нужно сформировать список из этих чисел
"""
n = int(input())
lst = list()
for i in range(n):
    lst.append(int(input()))
print(lst)
"""

n = int(input())
lst = [int(input()) for _ in range(n)]
print(lst)

