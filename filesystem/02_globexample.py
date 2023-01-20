from pathlib import Path

tmp_dir = Path('/etc/')
for fileobj in tmp_dir.glob('*.conf'):
    print(f'{fileobj.name} : ', end='')

    with fileobj.open('r') as data_file:
        data = data_file.readline().rstrip()
        print(data)
