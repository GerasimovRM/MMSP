lst = [1, 2, 3, 4, 5, 6, 7, 8]
del lst[::2]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst = lst[:-2]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
res = lst.pop(0)
print(lst, res)
