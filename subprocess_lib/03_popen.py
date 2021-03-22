from subprocess import (
    Popen, PIPE
)


def popen_ex():
    proc = Popen(
        ["sleep", "120"],
        stdout=PIPE
    )
    poll_result = proc.poll()
    proc.communicate()
    print('stdout:', repr(poll_result))


if __name__ == '__main__':
    popen_ex()
