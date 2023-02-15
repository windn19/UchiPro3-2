def get_sum():
    global total
    total = a + b + c
    print(total)


total = 0
a, b, c = 1, 2, 3
get_sum()
print(total)