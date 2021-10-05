# str, list, tuple, set, dict

# str
st = 'Привет'
number = 25
string_number = str(number)

# Операции: str + str, str * int, len(obj), in
print(st + string_number, st * number)
print(len(st))
print("ри" in st, "abc" in st)

print(st[0], st[5], st[-1], st[-3])
# print(st[6])  # IndexError: string index out of range

# st[0] = "п"  # TypeError: 'str' object does not support item assignment


