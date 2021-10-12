# вывести n (n > 2) первых чисел фибоначчи

n = int(input())
f1, f2 = 1, 1
print(f1)
print(f2)
for i in range(n - 2):
    f1, f2 = f2, f1 + f2
    print(f2)
