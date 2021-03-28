import sys


class MyObj:
    pass


class MyObjAttrs:
    def __init__(self, a):
        self.a = a


class MyObjAttrsSize:
    def __init__(self, a):
        self.a = a

    def __sizeof__(self):
        return object.__sizeof__(self) + \
               sum(sys.getsizeof(v) for v in self.__dict__.values())


def print_sizes():
    objects = [
        [], {}, (),
        '', 'a',
        MyObj(), MyObjAttrs('a'), MyObjAttrsSize('a')
    ]
    for o in objects:
        print(f'{type(o)}: {sys.getsizeof(o)}')


if __name__ == '__main__':
    print_sizes()
