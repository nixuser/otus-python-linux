import argparse
import sys
import time


def sleep_sec(x):
    print(sys.argv)
    time.sleep(x)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=int, default=60)
    args = parser.parse_args()

    sleep_sec(args.s)
