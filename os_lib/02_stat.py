import os
import sys
import time

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

# fd = os.open('test_file.txt', flags=os.O_RDONLY)
# stat_info = os.stat(fd)
# os.close(fd)

stat_info = os.stat(filename, follow_symlinks=False)

print(f'os.stat({filename}):')
print(f'  Size: {stat_info.st_size}')  # in bytes
print(f'  Permissions: {oct(stat_info.st_mode)}')  # man 2 stat
print(f'  Owner: {stat_info.st_uid}')  # dscl . -read /Users/<username> | grep UniqueID
print(f'  Created      : {time.ctime(stat_info.st_ctime)}')
print(f'  Last modified: {time.ctime(stat_info.st_mtime)}')
print(f'  Last accessed: {time.ctime(stat_info.st_atime)}')
