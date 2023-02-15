def number_generator(start, stop):
    while True:
        for i in range(start, stop + 1):
            yield i


start = int(input())
stop = int(input())
n = int(input())
g = number_generator(start, stop)
for i in range(n):
    print(next(g))
