import os
import sys

print(os.name)
print(os.environ)
print(os.getcwd())

if len(sys.argv) == 1:
    print(os.listdir(os.getcwd()))
else:
    print(os.listdir(sys.argv[1]))
