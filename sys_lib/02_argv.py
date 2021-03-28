import sys
print(f'list: {sys.argv}')

for i in range(len(sys.argv)):
    print(f'{i}, arg: {sys.argv[i]} {type(sys.argv[i])}')