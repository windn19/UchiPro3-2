# a = [1, 2, 3]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

a = [1, 2, 3]
b = iter(a)
while True:
    try:
        print(next(b))
    except StopIteration:
        print('Конец объекта')
        break