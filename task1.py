def counter():
    counts = 0

    def func():
        nonlocal counts
        counts += 1
        return counts

    return func


a, b, c = map(int, input().split())
total = 0
c1 = counter()
c2 = counter()
c3 = counter()
for i in range(a - 1):
    c1()
for i in range(b - 1):
    c2()
for i in range(c - 1):
    c3()
print(c1() + c2() + c3())
