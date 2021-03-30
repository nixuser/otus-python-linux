import sys


def stdout_ex():
    print('This goes to shell')
    out = sys.stdout
    print(f'sys.stdout: {sys.stdout}')
    with open('stdout.txt', 'w') as f:
        sys.stdout = f
        print(f'sys.stdout: {sys.stdout}')
        print('This goes to file')
    sys.stdout = out
    print('This goes to shell again')


def stdin_ex():
    orig_in = sys.stdin
    print(f'sys.stdin: {sys.stdin}')
    with open('sys_lib/stdin.txt') as f:
        sys.stdin = f
        print(f'sys.stdin: {sys.stdin}')
        print(sys.stdin.readline())
    sys.stdin = orig_in


if __name__ == '__main__':
    stdout_ex()
    # stdin_ex()
