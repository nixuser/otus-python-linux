import sys


def add_to_sys_path():
    print(f'Default paths: {sys.path}')
    sys.path.append('~/OTUS/python_linux/subprocess_lib')
    print(f'Updated paths: {sys.path}')


if __name__ == '__main__':
    add_to_sys_path()
