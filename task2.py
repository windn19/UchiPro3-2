def get_avg(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result / len([*args])

    return wrapper


@get_avg
def get_sum(*args):
    return sum(args)


args = map(int, input().split())
print(get_sum(*args))
