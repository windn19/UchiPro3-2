from pprint import pprint


def func(a):
    global x
    b = 4
    c = 5
    print(locals())


x = 1
y = 3
func(3)
pprint(globals())
