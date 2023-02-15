import time


def time_of_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(f'Время работы функции: {stop_time - start_time}')
        return result

    return wrapper


@time_of_func
def test():
    total = 0
    for i in range(10 ** 7):
        total += i
    return total


print(test())