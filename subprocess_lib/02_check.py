from subprocess import (
    check_call, check_output,
    STDOUT
)


def check_example():
    pass


def check_call_example():
    # Equivalent of subprocess.run(args, check=True)
    check_call(["false"])


def check_output_example():
    # Equivalent of subprocess.run(args, check=True, stdout=subprocess.PIPE)
    result = check_output(["ls", "-l"])
    print(f'stdout: {result}')


def check_output_stderr_to_stdout():
    # Capture standard error in the result
    result = check_output(["/bin/sh", "-c",
                          "ls -l non_existent_file ; exit 0"],
                          stderr=STDOUT)
    print(f'stdout: {result}')


def check_output_str_to_stdin():
    # Pass a string to the subprocess's stdin
    result = check_output(["sed", "-e", "s/foo/bar/"],
                          input=b"when in the course of fooman events\n")
    print(f'stdout: {result}')


if __name__ == '__main__':
    check_example()
    # check_call_example()
    # check_output_example()
    # check_output_stderr_to_stdout()
    # check_output_str_to_stdin()
