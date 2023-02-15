def fib(limit):
    f1, f2 = 1, 1
    while f1 < limit:
        yield f1
        f1, f2 = f2, f1 + f2


seq = fib(10)
for elem in seq:
    print(elem)
    