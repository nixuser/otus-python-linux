import os

path = '/home/vagrant'
with os.scandir(path) as it:
    for entry in it:
        if entry.name.startswith('.') and entry.is_file():
            print(entry.name)
