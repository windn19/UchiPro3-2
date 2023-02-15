def decorator_func(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


def test():
    print('Test')


test = decorator_func(test)
test()
