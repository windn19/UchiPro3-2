def decorator_func(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@decorator_func
def test(message):
    return message


print(test('тест'))
