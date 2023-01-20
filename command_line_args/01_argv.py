"""
Usage:
python3 01_argv.py
python3 01_argv.py a b c
python3 01_argv.py "aaa aaad" abc
"""
import sys

print(sys.argv[0])
print(len(sys.argv))
for arg in sys.argv:
    print(arg)

