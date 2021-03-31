from subprocess import (
    Popen, PIPE
)


def popen_ex():
    proc = Popen(["sleep", "90"], stdout=PIPE, stderr=PIPE)
    # Set and return returncode attribute. Otherwise, returns None.
    result = proc.poll()
    # Wait for process to terminate and set the returncode attribute.
    # Returns a tuple (stdout_data, stderr_data).
    # result = proc.communicate()
    print('return code:', repr(proc.returncode))
    print('result:', repr(result))


if __name__ == '__main__':
    popen_ex()
