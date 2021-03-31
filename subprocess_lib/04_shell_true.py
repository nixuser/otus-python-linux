from subprocess import (
    run, PIPE
)


def out_to_file():
    with open('out', 'w+') as f:
        run(["sleep", "120"], stdout=f)


def check_in_out():
    result = run(["sleep 120"], shell=True, stderr=PIPE, stdout=PIPE)
    # result = run(["sleep", "120"], stderr=PIPE, stdout=PIPE)
    print(result.stdout)
    print(result.stderr)


if __name__ == '__main__':
    # out_to_file()
    check_in_out()
