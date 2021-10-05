"""
st = input()

for i in range(0, len(st), 2):
    print(i, st[i])
"""

text = "Hello, world!"
print(text[0:5])
print(text[7:12])
print(text[3:])
print(text[:7])
print(text[-6:])
print(text[1::2])
print(text[::-1])

for sym in text[::2]:
    print(sym)
