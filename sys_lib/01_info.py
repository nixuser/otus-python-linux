import sys


def print_info():
    print(f'Python version: {sys.version}')
    print(f'Platform: {sys.platform}')
    print(f'Executable path: {sys.executable}')


if __name__ == '__main__':
    print_info()
