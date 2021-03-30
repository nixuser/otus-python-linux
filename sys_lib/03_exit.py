import sys


def bar():
    print('Exit from bar')
    sys.exit(1)


def foo():
    try:
        print('Try call bar')
        bar()
    except SystemExit as e:
        print(f'Handle {e}')
    finally:
        print('Finally exit from foo')


def bar_se():
    print('Exit from bar_se')
    raise SystemExit(1)


def foo_se():
    try:
        print('Try call bar_se')
        bar_se()
    except SystemExit as e:
        print(f'Handle {e}')
    finally:
        print('Finally exit from foo_se')


if __name__ == '__main__':
    foo()
    # foo_se()
