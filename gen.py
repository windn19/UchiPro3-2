def generator():
    i = 1
    yield i
    i += 1
    yield i
    i += 1
    yield i


g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))