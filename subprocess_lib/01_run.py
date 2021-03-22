from subprocess import (
    run, PIPE
)


def run_example():
    # By default, stdout and stderr are not captured, and those attributes will be None
    result = run(["ls", "-l"])
    print(result)
    print(result.stdout)
    print(result.stderr)


def exit_code_non_zero():
    # If check is True and the exit code was non-zero, it raises a CalledProcessError
    run(["false"], check=True)


def capture_err_and_out():
    # Capture standard error and standard output in the result
    result = run(["ls", "-l"], stderr=PIPE, stdout=PIPE)
    print(result.stderr)
    print(result.stdout)


def capture_err_and_out_2():
    # Equivalent of stderr=PIPE, stdout=PIPE
    result = run(["ls", "-l"], capture_output=True)
    print(result.stderr)
    print(result.stdout)


def timeout():
    # Using timeout
    result = run(["sleep", "5"], timeout=6)
    print(result.returncode)


def shell():
    # If shell=True, the command string is interpreted as a raw shell command
    run(["echo", "$HOME"])
    run(["echo $HOME"], shell=True)
    run(["echo $HOME | wc -c"], shell=True)


if __name__ == '__main__':
    run_example()
    # exit_code_non_zero()
    # capture_err_and_out()
    # capture_err_and_out_2()
    # timeout_example()
    # shell()
