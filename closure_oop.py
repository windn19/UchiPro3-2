def mul(x):
    def func(y):
        return x * y

    return func


class Mul:
    def __init__(self, a):
        self.a = a

    def __call__(self, b, *args, **kwargs):
        return self.a * b


mul5 = mul(5)
mul51 = Mul(5)
print(f'{mul5(3):^4} | {mul51(3):^4} |')
print(f'{mul5(5):^4} | {mul51(5):^4} |')
print(f'{mul5(9):^4} | {mul51(9):^4} |')
