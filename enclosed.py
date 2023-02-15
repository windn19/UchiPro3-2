def f():
    def g():
        z = 'local'
        print(x, y, z)

    y = 'enclosing'
    print(x)
    g()


x = 'global'
f()
