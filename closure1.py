def hello():
    def func():
        print(message)

    message = 'Привет'
    return func


f = hello()
f()
