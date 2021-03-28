import sys


def stdout_ex():
    print('This goes to shell')
    out = sys.stdout
    with open('stdout.txt', 'w') as f:
        sys.stdout = f
        f.write('This goes to file')
    sys.stdout = out
    print('This goes to shell again')


def stdin_ex():
    stdin = sys.stdin
    with open('sys_lib/stdin.txt') as f:
        sys.stdin = f
        print(sys.stdin.readline())
    sys.stdin = stdin


if __name__ == '__main__':
    stdout_ex()
    # stdin_ex()
