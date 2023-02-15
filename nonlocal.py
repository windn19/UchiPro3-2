def f():
    def g():
        nonlocal x
        print(x)
        x = 'change enclosing'

    x = 'enclosing'
    g()
    print(x)

x = 0
f()
print(x)
