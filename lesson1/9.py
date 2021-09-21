# range(N) => 0, .. N - 1
# range(a, b) => a, a + 1, .. b - 2, b - 1
# range(a, b, step) => a + step, a + 2 * step, ..

for i in range(10):  # 0, 1, 2, 3, .., 8, 9
    print(i, i ** 2)


for i in range(0, 100, 4):
    print(i)
