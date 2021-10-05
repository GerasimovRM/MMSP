# int, float, str, bool

# int -> str; str -> int
# float -> str; str -> float

j = 7
k = str(j)

a = float(input())
b = float(input())
print(a + b, a - b, a * b, a / b, a ** b)

c = 7
d = 8.4
print(c + d, type(c + d))

# bool: True, False
# все что пустое и все что 0 => False, все остальное - True
print(bool("123"), bool(""), bool(123), bool(0.0))
print(bool("0"))


